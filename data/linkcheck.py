#!/usr/bin/env python3
"""data/enriched.json の paper/page/arXiv/GitHub リンク死活を確認する。"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ENRICHED = Path("data/enriched.json")
REPORT = Path("docs/linkcheck-report.md")
USER_AGENT = "awesome-ai-survey-papers-linkcheck/1.0"

# 出版社/CDN の bot 拒否でよく返るコード。リンク自体は有効なため「blocked(生存扱い)」とし、
# CI を失敗させない（本物の 404/DNS/タイムアウト/5xx のみ dead として失敗させる）。
BLOCKED_CODES = {401, 403, 406, 429, 451}

_ARXIV_LOCK = threading.Lock()
_ARXIV_LAST_REQUEST = 0.0


@dataclass(frozen=True)
class Target:
    kind: str
    value: str
    url: str


@dataclass
class CheckResult:
    kind: str
    value: str
    url: str
    status: str  # "alive" | "blocked" | "dead"
    detail: str
    titles: list[str]

    @property
    def ok(self) -> bool:
        # blocked はリンク有効とみなす（dead のみ失敗扱い）
        return self.status in ("alive", "blocked")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=8, help="maximum parallel checks")
    parser.add_argument("--timeout", type=float, default=15.0, help="per-request timeout in seconds")
    parser.add_argument("--report", default=str(REPORT), help="Markdown report path")
    parser.add_argument("--limit", type=int, default=0, help="debug: only check the first N entries")
    return parser.parse_args()


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def arxiv_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/abs/{arxiv_id}"


def throttle_if_arxiv(url: str) -> None:
    global _ARXIV_LAST_REQUEST
    host = urllib.parse.urlparse(url).netloc.lower()
    if host not in {"arxiv.org", "www.arxiv.org"}:
        return
    with _ARXIV_LOCK:
        elapsed = time.monotonic() - _ARXIV_LAST_REQUEST
        wait = 0.15 - elapsed
        if wait > 0:
            time.sleep(wait)
        _ARXIV_LAST_REQUEST = time.monotonic()


def request_once(url: str, method: str, timeout: float) -> tuple[str, str]:
    throttle_if_arxiv(url)
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,*/*"}
    req = urllib.request.Request(url, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", resp.getcode())
        if 200 <= status < 400:
            return "alive", f"HTTP {status}"
        return "dead", f"HTTP {status}"


def check_http_url(url: str, timeout: float) -> tuple[str, str]:
    if not url.startswith(("http://", "https://")):
        return "dead", "invalid URL scheme"
    try:
        return request_once(url, "HEAD", timeout)
    except urllib.error.HTTPError as exc:
        # HEAD を拒否するが GET は通るホストがあるため GET で再試行。
        if exc.code in {403, 405, 406, 501}:
            try:
                return request_once(url, "GET", timeout)
            except urllib.error.HTTPError as get_exc:
                if get_exc.code in BLOCKED_CODES:
                    return "blocked", f"HTTP {get_exc.code} (bot-blocked; link valid)"
                return "dead", f"HTTP {get_exc.code}"
            except Exception as get_exc:  # noqa: BLE001 - keep report detail explicit
                return "dead", error_detail(get_exc)
        if exc.code in BLOCKED_CODES:
            return "blocked", f"HTTP {exc.code} (bot-blocked; link valid)"
        return "dead", f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - linkcheck should report, not crash
        return "dead", error_detail(exc)


def error_detail(exc: BaseException) -> str:
    text = str(exc).strip()
    return f"{exc.__class__.__name__}: {text}" if text else exc.__class__.__name__


def check_github_repo(repo: str, timeout: float) -> tuple[str, str]:
    if "/" not in repo:
        return "dead", "invalid owner/repo"
    if shutil.which("gh") is None:
        return "dead", "gh CLI not found"
    env = os.environ.copy()
    if "GH_TOKEN" not in env and "GITHUB_TOKEN" in env:
        env["GH_TOKEN"] = env["GITHUB_TOKEN"]
    try:
        completed = subprocess.run(
            ["gh", "api", f"repos/{repo}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            env=env,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return False, error_detail(exc)
    if completed.returncode == 0:
        return "alive", "gh api ok"
    detail = completed.stderr.strip().splitlines()
    return "dead", detail[-1] if detail else f"gh api exit {completed.returncode}"


def collect_targets(items: list[dict]) -> tuple[dict[Target, set[str]], int]:
    targets: dict[Target, set[str]] = {}
    for it in items:
        title = it.get("title", "")
        if it.get("paper"):
            target = Target("paper", it["paper"], it["paper"])
            targets.setdefault(target, set()).add(title)
        if it.get("page"):
            target = Target("page", it["page"], it["page"])
            targets.setdefault(target, set()).add(title)
        if it.get("arxiv"):
            target = Target("arxiv", it["arxiv"], arxiv_url(it["arxiv"]))
            targets.setdefault(target, set()).add(title)
        if it.get("github"):
            repo = it["github"]
            target = Target("github", repo, f"https://github.com/{repo}")
            targets.setdefault(target, set()).add(title)
    return targets, len(items)


def run_checks(target_titles: dict[Target, set[str]], workers: int, timeout: float) -> list[CheckResult]:
    results: list[CheckResult] = []
    future_targets = {}
    http_future_by_url = {}

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        for target in target_titles:
            if target.kind in {"paper", "page", "arxiv"}:
                future = http_future_by_url.get(target.url)
                if future is None:
                    future = pool.submit(check_http_url, target.url, timeout)
                    http_future_by_url[target.url] = future
                future_targets.setdefault(future, []).append(target)
            else:
                future = pool.submit(check_github_repo, target.value, timeout)
                future_targets.setdefault(future, []).append(target)

        for future in as_completed(future_targets):
            try:
                status, detail = future.result()
            except Exception as exc:  # noqa: BLE001
                status, detail = "dead", error_detail(exc)
            for target in future_targets[future]:
                titles = sorted(target_titles[target])
                results.append(CheckResult(target.kind, target.value, target.url, status, detail, titles))

    return sorted(results, key=lambda r: (r.kind, r.value))


def write_report(
    path: Path,
    results: list[CheckResult],
    checked_entry_count: int,
    source_entry_count: int,
    limit: int,
) -> None:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    alive = sum(1 for r in results if r.status == "alive")
    blocked = sum(1 for r in results if r.status == "blocked")
    dead = sum(1 for r in results if r.status == "dead")
    by_kind = {}
    for r in results:
        stats = by_kind.setdefault(r.kind, {"alive": 0, "blocked": 0, "dead": 0})
        stats[r.status] += 1

    lines = [
        "# Link Check Report",
        "",
        f"- Generated: {generated}",
        f"- Source entries: {source_entry_count}",
        f"- Checked entries: {checked_entry_count}",
        f"- Checks: {len(results)}",
        f"- Alive: {alive}",
        f"- Blocked (bot-blocked, link valid): {blocked}",
        f"- Dead: {dead}",
        "",
        "## Summary",
        "",
        "| Kind | Alive | Blocked | Dead |",
        "|---|---:|---:|---:|",
    ]
    if limit:
        lines.insert(8, f"- Limit: first {limit} entries (debug run)")
    for kind in sorted(by_kind):
        stats = by_kind[kind]
        lines.append(f"| {kind} | {stats['alive']} | {stats['blocked']} | {stats['dead']} |")

    blocked_rows = [r for r in results if r.status == "blocked"]
    if blocked_rows:
        lines.extend([
            "",
            "## Blocked (treated as alive — publisher/CDN rejects automated requests)",
            "",
            "| Kind | Target | Detail | Example title |",
            "|---|---|---|---|",
        ])
        for r in blocked_rows:
            target = f"[{md_escape(r.value)}]({r.url})" if r.url.startswith("http") else md_escape(r.value)
            title = md_escape(r.titles[0]) + (f" (+{len(r.titles) - 1} more)" if len(r.titles) > 1 else "")
            lines.append(f"| {r.kind} | {target} | {md_escape(r.detail)} | {title} |")

    lines.extend(["", "## Dead Links", ""])

    dead_rows = [r for r in results if r.status == "dead"]
    if not dead_rows:
        lines.append("No dead links detected.")
    else:
        lines.extend(
            [
                "| Kind | Target | Detail | Example title |",
                "|---|---|---|---|",
            ]
        )
        for r in dead_rows:
            target = f"[{md_escape(r.value)}]({r.url})" if r.url.startswith("http") else md_escape(r.value)
            title = md_escape(r.titles[0])
            if len(r.titles) > 1:
                title += f" (+{len(r.titles) - 1} more)"
            lines.append(f"| {r.kind} | {target} | {md_escape(r.detail)} | {title} |")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    args = parse_args()
    all_items = json.loads(ENRICHED.read_text())
    items = all_items
    if args.limit:
        items = items[: args.limit]

    target_titles, checked_entry_count = collect_targets(items)
    results = run_checks(target_titles, args.workers, args.timeout)
    report_path = Path(args.report)
    write_report(report_path, results, checked_entry_count, len(all_items), args.limit)

    dead = [r for r in results if r.status == "dead"]
    blocked = [r for r in results if r.status == "blocked"]
    print(f"linkcheck: {len(results)} checks, {len(results) - len(dead) - len(blocked)} alive, "
          f"{len(blocked)} blocked, {len(dead)} dead")
    print(f"report: {report_path}")
    if dead:
        print("dead links:")
        for r in dead[:20]:
            print(f"- {r.kind} {r.value}: {r.detail}")
        if len(dead) > 20:
            print(f"... and {len(dead) - 20} more")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
