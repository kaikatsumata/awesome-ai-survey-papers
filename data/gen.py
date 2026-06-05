#!/usr/bin/env python3
"""enriched.json から README.md（分類済みリスト）と docs/research-notes.md（全調査結果）を生成。"""
import json
from collections import defaultdict, Counter
from datetime import datetime, timezone

ENRICHED = "data/enriched.json"
README = "README.md"
NOTES = "docs/research-notes.md"

# 分野表示名・絵文字・並び順
FIELD_META = {
    "llm": ("大規模言語モデル (LLM)", "🧠"),
    "genai": ("生成AI・拡散モデル", "🎨"),
    "multimodal": ("マルチモーダル・視覚言語", "🖼️"),
    "nlp": ("自然言語処理 (NLP)", "💬"),
    "speech": ("音声・信号処理", "🔊"),
    "cv": ("コンピュータビジョン (CV)", "👁️"),
    "ml": ("機械学習 (一般)", "📈"),
    "learning-theory": ("学習理論", "📐"),
    "rl": ("強化学習 (RL)", "🎮"),
    "robotics": ("ロボティクス・身体性", "🤖"),
    "multi-agent": ("マルチエージェント", "👥"),
    "gnn": ("グラフニューラルネット (GNN)", "🕸️"),
    "knowledge": ("知識表現・知識グラフ", "🔗"),
    "causal": ("因果推論", "🎯"),
    "time-series": ("時系列・時空間", "⏱️"),
    "data-mining": ("データマイニング", "⛏️"),
    "database": ("データベース・データ管理", "🗄️"),
    "ir": ("情報検索 (IR)", "🔍"),
    "recsys": ("推薦システム", "🛒"),
    "web": ("Web・ソーシャル", "🌐"),
    "trustworthy": ("信頼できるAI (公平性・XAI・安全性)", "🛡️"),
    "federated": ("連合学習", "📡"),
    "hci": ("HCI・ヒューマンAI", "🖐️"),
    "evolutionary": ("進化計算", "🧬"),
    "tcs": ("理論計算機科学", "🔢"),
    "ai4science": ("AI for Science", "🔬"),
    "ai-general": ("人工知能 (全般)", "🌟"),
    "neural-nets": ("ニューラルネット基礎", "🧩"),
    "applications": ("応用・横断領域", "🏭"),
    "data-eval": ("データ中心AI・評価", "📊"),
}
FIELD_ORDER = list(FIELD_META.keys())


def load():
    return json.load(open(ENRICHED))


def fresh_marker(pushed):
    if not pushed:
        return ""
    try:
        d = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
    except Exception:
        return ""
    months = (datetime.now(timezone.utc) - d).days / 30.0
    if months <= 6:
        return "🟢"
    if months <= 18:
        return "🟡"
    return "🔴"


def fmt_entry(it):
    title = it["title"].strip().replace("\n", " ")
    paper = it.get("paper") or (f"https://arxiv.org/abs/{it['arxiv']}" if it.get("arxiv") else "")
    line = f"- [{title}]({paper})" if paper else f"- {title}"
    meta = []
    if it.get("venue"):
        meta.append(it["venue"])
    if it.get("year"):
        meta.append(str(it["year"]))
    if meta:
        line += f" — *{' '.join(meta)}*"
    if it.get("citations") is not None:
        line += f" · 📈{it['citations']}"
    if it.get("note"):
        line += f"。{it['note']}"
    extras = []
    if it.get("github"):
        gh = it["github"]
        star = f"⭐{it['github_stars']}" if it.get("github_stars") is not None else ""
        fm = fresh_marker(it.get("github_pushed"))
        extras.append(f"[`{gh}`](https://github.com/{gh}) {star}{fm}".strip())
    if it.get("page"):
        extras.append(f"[project]({it['page']})")
    if extras:
        line += " — " + " · ".join(extras)
    return line


def sort_key(it):
    return (-(it.get("citations") or 0), -(it.get("year") or 0))


def anchor(text):
    import re
    a = text.lower()
    a = re.sub(r"[^\w\s\-ぁ-んァ-ヶ一-龠ー]", "", a)
    a = a.replace(" ", "-")
    return a


def gen_readme(items):
    by_field = defaultdict(lambda: defaultdict(list))
    for it in items:
        by_field[it.get("field", "ai-general")][it.get("subfield", "その他")].append(it)

    total = len(items)
    n_gh = sum(1 for it in items if it.get("github"))
    n_fields = len([f for f in by_field])
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    out = []
    out.append("# Awesome AI Survey Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    out.append("> AI関連分野のトップ会議・トップジャーナル・arXiv で公開された**サーベイ論文 "
               "(survey / review / overview)** の厳選キュレーション。研究サーベイの出発点として、"
               "良質で網羅的なレビュー論文へ最短で辿り着くことを目的とします。\n")
    out.append(f"**{total} 本のサーベイ論文** / {n_fields} 分野 / companion リポジトリ {n_gh} 件付き。"
               f"最終更新 {today}。\n")
    out.append("各項目は `[タイトル](論文URL) — *venue 年* · 📈被引用数。説明 — "
               "[`companion repo`](github) ⭐star🟢鮮度 · [project](ページ)` の形式。\n")
    out.append("凡例: 📈 被引用数 (Semantic Scholar) · ⭐ GitHub star · "
               "鮮度 🟢直近6ヶ月 / 🟡18ヶ月内 / 🔴それ以前（サーベイ companion は鮮度が低くても"
               "網羅性・権威性で価値があります）。\n")

    # 全調査結果は別ドキュメント
    out.append("> 📑 収集の全メタデータ・統計・調査手法は [`docs/research-notes.md`](docs/research-notes.md) を参照。\n")

    # TOC
    out.append("## 目次\n")
    ordered_fields = [f for f in FIELD_ORDER if f in by_field] + \
                     [f for f in by_field if f not in FIELD_ORDER]
    for f in ordered_fields:
        disp, emoji = FIELD_META.get(f, (f, "•"))
        cnt = sum(len(v) for v in by_field[f].values())
        head = f"{emoji} {disp}"
        out.append(f"- [{head}](#{anchor(head)}) ({cnt})")
    out.append("")

    # 本体
    for f in ordered_fields:
        disp, emoji = FIELD_META.get(f, (f, "•"))
        out.append(f"## {emoji} {disp}\n")
        subs = by_field[f]
        for sub in sorted(subs.keys()):
            entries = sorted(subs[sub], key=sort_key)
            out.append(f"### {sub}\n")
            for it in entries:
                out.append(fmt_entry(it))
            out.append("")

    out.append("## 貢献\n")
    out.append("追加・修正は [`contributing.md`](contributing.md) を参照。サーベイ論文 "
               "(survey/review/overview) のみを対象とし、実在検証 (arXiv/DOI/GitHub) を経たもののみ掲載します。\n")
    out.append("## ライセンス\n")
    out.append("[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) "
               "本リスト（キュレーション）は CC0 (パブリックドメイン)。各論文の著作権は原著者に帰属します。\n")
    open(README, "w").write("\n".join(out))
    return total, n_gh, n_fields, ordered_fields, by_field


def gen_notes(items, ordered_fields, by_field):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = []
    out.append("# 調査ノート — Awesome AI Survey Papers\n")
    out.append(f"本ドキュメントは収集した全サーベイ論文のメタデータ・統計・調査手法をまとめたもの。"
               f"READMEは分類済みリストに徹し、ここに全調査結果を集約する。最終更新 {today}。\n")

    # 統計
    out.append("## 統計\n")
    out.append(f"- 総数: **{len(items)}** 本")
    out.append(f"- 分野数: {len(by_field)}")
    out.append(f"- companion GitHub 付き: {sum(1 for it in items if it.get('github'))} 件")
    out.append(f"- arXiv ID あり: {sum(1 for it in items if it.get('arxiv'))} 件")
    out.append(f"- 被引用数取得済み: {sum(1 for it in items if it.get('citations') is not None)} 件")
    years = Counter(it.get("year") for it in items if it.get("year"))
    out.append(f"- 出版年の分布: " + ", ".join(f"{y}:{c}" for y, c in sorted(years.items())))
    out.append("")

    out.append("### 分野別件数\n")
    out.append("| 分野 | 件数 | サブ分野数 |")
    out.append("|---|---:|---:|")
    for f in ordered_fields:
        disp, _ = FIELD_META.get(f, (f, ""))
        cnt = sum(len(v) for v in by_field[f].values())
        out.append(f"| {disp} | {cnt} | {len(by_field[f])} |")
    out.append("")

    # 高被引用トップ
    cited = sorted([it for it in items if it.get("citations") is not None],
                   key=lambda x: -x["citations"])[:30]
    if cited:
        out.append("## 被引用数トップ30\n")
        out.append("| 被引用 | タイトル | venue | 年 |")
        out.append("|---:|---|---|---:|")
        for it in cited:
            out.append(f"| {it['citations']} | {it['title'][:70]} | {it.get('venue','')} | {it.get('year','')} |")
        out.append("")

    # companion repos
    ghs = sorted([it for it in items if it.get("github")],
                 key=lambda x: -(x.get("github_stars") or 0))
    if ghs:
        out.append("## companion GitHub リポジトリ（star順・実在検証済み）\n")
        out.append("| ⭐star | repo | 最終更新 | 論文 |")
        out.append("|---:|---|---|---|")
        for it in ghs:
            out.append(f"| {it.get('github_stars','?')} | "
                       f"[{it['github']}](https://github.com/{it['github']}) | "
                       f"{(it.get('github_pushed') or '')[:10]} | {it['title'][:50]} |")
        out.append("")

    # 全エントリ一覧（分野ごと）
    out.append("## 全エントリ一覧\n")
    for f in ordered_fields:
        disp, emoji = FIELD_META.get(f, (f, "•"))
        out.append(f"### {emoji} {disp}\n")
        rows = sorted(by_field_flat(by_field[f]), key=sort_key)
        out.append("| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |")
        out.append("|---|---|---|---:|---|---:|---|")
        for it in rows:
            ax = it.get("arxiv") or ""
            cit = it.get("citations") if it.get("citations") is not None else ""
            gh = it.get("github") or ""
            out.append(f"| {it['title'][:60]} | {it.get('authors','')[:25]} | {it.get('venue','')} | "
                       f"{it.get('year','')} | {ax} | {cit} | {gh} |")
        out.append("")

    open(NOTES, "w").write("\n".join(out))


def by_field_flat(subdict):
    r = []
    for v in subdict.values():
        r.extend(v)
    return r


def main():
    items = load()
    total, n_gh, n_fields, ordered_fields, by_field = gen_readme(items)
    gen_notes(items, ordered_fields, by_field)
    print(f"README.md: {total} papers, {n_fields} fields, {n_gh} companion repos")
    print(f"docs/research-notes.md generated")


if __name__ == "__main__":
    main()
