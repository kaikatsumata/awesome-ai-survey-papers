#!/usr/bin/env python3
"""data/raw/*.json のサーベイ論文を統合・重複排除し、API でメタデータを補強して
enriched.json を生成する。

処理:
  1. data/raw/*.json を全マージ
  2. arXiv ID（無ければ正規化タイトル）で重複排除
  3. companion GitHub を gh api で実在確認・stars/pushed_at 取得（並列）
  4. Semantic Scholar batch API で被引用数を取得（best-effort）
  5. enriched.json 出力 + 統計レポート
"""
import json
import re
import glob
import time
import subprocess
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

RAW_GLOB = "data/raw/*.json"
OUT = "data/enriched.json"


def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())


def load_all():
    items = []
    for path in sorted(glob.glob(RAW_GLOB)):
        try:
            data = json.load(open(path))
        except Exception as e:
            print(f"  WARN: {path} 読み込み失敗: {e}")
            continue
        if isinstance(data, dict):
            data = data.get("papers") or data.get("surveys") or list(data.values())
        for it in data:
            if isinstance(it, dict) and it.get("title"):
                it["_src"] = path.split("/")[-1]
                items.append(it)
    return items


def dedup(items):
    seen = {}
    order = []
    for it in items:
        key = ("ax:" + it["arxiv"]) if it.get("arxiv") else ("ti:" + norm_title(it["title"]))
        if key in seen:
            # 既存にgithub/pageが無く新規にあれば補完
            ex = seen[key]
            for f in ("github", "page", "arxiv"):
                if not ex.get(f) and it.get(f):
                    ex[f] = it[f]
            continue
        seen[key] = it
        order.append(key)
    return [seen[k] for k in order]


def check_github(full_name):
    if not full_name:
        return None
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{full_name}",
             "--jq", "{full_name:.full_name, stars:.stargazers_count, pushed:.pushed_at, archived:.archived}"],
            capture_output=True, text=True, timeout=30,
        )
        if out.returncode != 0:
            return {"status": "404"}
        d = json.loads(out.stdout)
        return {"status": "ok", "canonical": d["full_name"], "stars": d["stars"],
                "pushed": d["pushed"], "archived": d["archived"]}
    except Exception as e:
        return {"status": "err", "err": str(e)[:80]}


def enrich_github(items):
    gh_items = [it for it in items if it.get("github")]
    with ThreadPoolExecutor(max_workers=12) as ex:
        results = list(ex.map(lambda it: check_github(it["github"]), gh_items))
    for it, r in zip(gh_items, results):
        if not r:
            continue
        if r["status"] == "ok":
            it["github"] = r["canonical"]
            it["github_stars"] = r["stars"]
            it["github_pushed"] = r["pushed"]
            it["github_archived"] = r["archived"]
        else:
            # 実在しないcompanionは外す（捏造排除）
            it["github_invalid"] = it.pop("github")


def fetch_citations(items):
    """Semantic Scholar batch API で被引用数取得（best-effort, 失敗は無視）。"""
    ax = [it for it in items if it.get("arxiv")]
    ids = [f"ARXIV:{it['arxiv']}" for it in ax]
    got = 0
    for i in range(0, len(ids), 100):
        chunk = ids[i:i + 100]
        chunk_items = ax[i:i + 100]
        # 429対策: 指数バックオフで最大4回再試行
        for attempt in range(4):
            try:
                req = urllib.request.Request(
                    "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,year,venue",
                    data=json.dumps({"ids": chunk}).encode(),
                    headers={"Content-Type": "application/json"},
                )
                with urllib.request.urlopen(req, timeout=40) as resp:
                    arr = json.loads(resp.read())
                for it, rec in zip(chunk_items, arr):
                    if rec and rec.get("citationCount") is not None:
                        it["citations"] = rec["citationCount"]
                        got += 1
                time.sleep(2)  # レート制限緩和
                break
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < 3:
                    time.sleep(5 * (attempt + 1))
                    continue
                print(f"  WARN: S2 batch {i}: HTTP {e.code}")
                break
            except Exception as e:
                print(f"  WARN: S2 batch {i}: {str(e)[:80]}")
                break
    return got


def main():
    items = load_all()
    print(f"merged={len(items)}")
    items = dedup(items)
    print(f"deduped={len(items)}")
    enrich_github(items)
    gh_ok = sum(1 for it in items if it.get("github"))
    gh_bad = sum(1 for it in items if it.get("github_invalid"))
    print(f"github: ok={gh_ok} invalid_removed={gh_bad}")
    cited = fetch_citations(items)
    print(f"citations fetched={cited}")
    json.dump(items, open(OUT, "w"), ensure_ascii=False, indent=2)
    # 統計
    from collections import Counter
    fields = Counter(it.get("field", "?") for it in items)
    print("by field:", dict(sorted(fields.items(), key=lambda x: -x[1])))
    print(f"wrote {OUT} ({len(items)} entries)")


if __name__ == "__main__":
    main()
