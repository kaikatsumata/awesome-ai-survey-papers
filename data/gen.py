#!/usr/bin/env python3
"""enriched.json から多言語 README と docs/research-notes.md を生成する。"""
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ENRICHED = Path("data/enriched.json")
NOTES = Path("docs/research-notes.md")

# (lang_code, output_file, autonym)
LANGS = [
    ("ja", "README.md", "日本語"),
    ("en", "README.en.md", "English"),
]

STR = {
    "ja": {
        "lang_label": "Languages",
        "title": "Awesome AI Survey Papers",
        "description": (
            "AI関連分野のトップ会議・トップジャーナル・arXiv で公開された"
            "**サーベイ論文 (survey / review / overview)** の厳選キュレーション。"
            "研究サーベイの出発点として、良質で網羅的なレビュー論文へ最短で"
            "辿り着くことを目的とします。"
        ),
        "summary": (
            "**{total} 本のサーベイ論文** / {n_fields} 分野 / companion リポジトリ "
            "{n_gh} 件付き。最終更新 {today}。"
        ),
        "entry_format": (
            "各項目は `[タイトル](論文URL) — *venue 年* · 📈被引用数。説明 — "
            "[`companion repo`](github) ⭐star🟢鮮度 · [project](ページ)` の形式。"
        ),
        "legend": (
            "凡例: 📈 被引用数 (Semantic Scholar) · ⭐ GitHub star · "
            "鮮度 🟢直近6ヶ月 / 🟡18ヶ月内 / 🔴それ以前（サーベイ companion は"
            "鮮度が低くても網羅性・権威性で価値があります）。"
        ),
        "notes_ref": (
            "> 📑 収集の全メタデータ・統計・調査手法は "
            "[`docs/research-notes.md`](docs/research-notes.md) を参照。"
        ),
        "toc": "目次",
        "contribution": "貢献",
        "contribution_body": (
            "追加・修正は [`contributing.md`](contributing.md) を参照。サーベイ論文 "
            "(survey/review/overview) のみを対象とし、実在検証 (arXiv/DOI/GitHub) "
            "を経たもののみ掲載します。"
        ),
        "license": "ライセンス",
        "license_body": (
            "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) "
            "本リスト（キュレーション）は CC0 (パブリックドメイン)。"
            "各論文の著作権は原著者に帰属します。"
        ),
        "project": "project",
        "note_separator": "。",
    },
    "en": {
        "lang_label": "Languages",
        "title": "Awesome AI Survey Papers",
        "description": (
            "A curated collection of high-quality **survey, review, and overview papers** "
            "from top AI conferences, journals, and arXiv. It is designed as a fast "
            "starting point for finding authoritative review papers across AI research."
        ),
        "summary": (
            "**{total} survey papers** across {n_fields} fields, with {n_gh} companion "
            "repositories. Last updated {today}."
        ),
        "entry_format": (
            "Each item uses the format `[title](paper URL) — *venue year* · 📈 citations"
            " — note — [`companion repo`](github) ⭐stars🟢freshness · [project](page)`."
        ),
        "legend": (
            "Legend: 📈 citation count (Semantic Scholar) · ⭐ GitHub stars · freshness "
            "🟢 updated within 6 months / 🟡 within 18 months / 🔴 older. Survey companion "
            "repositories may still be valuable for coverage and authority even when stale."
        ),
        "notes_ref": (
            "> 📑 Full metadata, statistics, and collection methodology are available in "
            "[`docs/research-notes.md`](docs/research-notes.md) (Japanese)."
        ),
        "toc": "Table of Contents",
        "contribution": "Contributing",
        "contribution_body": (
            "See [`contributing.md`](contributing.md) for additions and corrections. "
            "Only survey, review, and overview papers are included, and entries should be "
            "verified against arXiv/DOI/GitHub before publication."
        ),
        "license": "License",
        "license_body": (
            "[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) "
            "This curated list is released under CC0 (public domain). Copyright for each "
            "paper belongs to its original authors."
        ),
        "project": "project",
        "note_separator": " — ",
    },
}

# 分野表示名と絵文字。FIELD_META は後方互換のため日本語表示名を保持する。
FIELD_I18N = {
    "llm": {"ja": "大規模言語モデル (LLM)", "en": "Large Language Models (LLM)"},
    "genai": {"ja": "生成AI・拡散モデル", "en": "Generative AI and Diffusion Models"},
    "multimodal": {"ja": "マルチモーダル・視覚言語", "en": "Multimodal and Vision-Language AI"},
    "nlp": {"ja": "自然言語処理 (NLP)", "en": "Natural Language Processing (NLP)"},
    "speech": {"ja": "音声・信号処理", "en": "Speech and Signal Processing"},
    "cv": {"ja": "コンピュータビジョン (CV)", "en": "Computer Vision (CV)"},
    "ml": {"ja": "機械学習 (一般)", "en": "Machine Learning (General)"},
    "learning-theory": {"ja": "学習理論", "en": "Learning Theory"},
    "rl": {"ja": "強化学習 (RL)", "en": "Reinforcement Learning (RL)"},
    "robotics": {"ja": "ロボティクス・身体性", "en": "Robotics and Embodied AI"},
    "multi-agent": {"ja": "マルチエージェント", "en": "Multi-Agent Systems"},
    "gnn": {"ja": "グラフニューラルネット (GNN)", "en": "Graph Neural Networks (GNN)"},
    "knowledge": {"ja": "知識表現・知識グラフ", "en": "Knowledge Representation and Knowledge Graphs"},
    "causal": {"ja": "因果推論", "en": "Causal Inference"},
    "time-series": {"ja": "時系列・時空間", "en": "Time Series and Spatio-Temporal AI"},
    "data-mining": {"ja": "データマイニング", "en": "Data Mining"},
    "database": {"ja": "データベース・データ管理", "en": "Databases and Data Management"},
    "ir": {"ja": "情報検索 (IR)", "en": "Information Retrieval (IR)"},
    "recsys": {"ja": "推薦システム", "en": "Recommender Systems"},
    "web": {"ja": "Web・ソーシャル", "en": "Web and Social Computing"},
    "trustworthy": {
        "ja": "信頼できるAI (公平性・XAI・安全性)",
        "en": "Trustworthy AI (Fairness, XAI, and Safety)",
    },
    "federated": {"ja": "連合学習", "en": "Federated Learning"},
    "hci": {"ja": "HCI・ヒューマンAI", "en": "HCI and Human-AI Interaction"},
    "evolutionary": {"ja": "進化計算", "en": "Evolutionary Computation"},
    "tcs": {"ja": "理論計算機科学", "en": "Theoretical Computer Science"},
    "ai4science": {"ja": "AI for Science", "en": "AI for Science"},
    "ai-general": {"ja": "人工知能 (全般)", "en": "Artificial Intelligence (General)"},
    "neural-nets": {"ja": "ニューラルネット基礎", "en": "Neural Network Foundations"},
    "applications": {"ja": "応用・横断領域", "en": "Applications and Cross-Domain AI"},
    "data-eval": {"ja": "データ中心AI・評価", "en": "Data-Centric AI and Evaluation"},
}

FIELD_EMOJI = {
    "llm": "🧠",
    "genai": "🎨",
    "multimodal": "🖼️",
    "nlp": "💬",
    "speech": "🔊",
    "cv": "👁️",
    "ml": "📈",
    "learning-theory": "📐",
    "rl": "🎮",
    "robotics": "🤖",
    "multi-agent": "👥",
    "gnn": "🕸️",
    "knowledge": "🔗",
    "causal": "🎯",
    "time-series": "⏱️",
    "data-mining": "⛏️",
    "database": "🗄️",
    "ir": "🔍",
    "recsys": "🛒",
    "web": "🌐",
    "trustworthy": "🛡️",
    "federated": "📡",
    "hci": "🖐️",
    "evolutionary": "🧬",
    "tcs": "🔢",
    "ai4science": "🔬",
    "ai-general": "🌟",
    "neural-nets": "🧩",
    "applications": "🏭",
    "data-eval": "📊",
}
FIELD_META = {k: (v["ja"], FIELD_EMOJI[k]) for k, v in FIELD_I18N.items()}
FIELD_ORDER = list(FIELD_I18N.keys())


def load():
    return json.loads(ENRICHED.read_text())


def normalize_title(title):
    key = title.strip().lower()
    key = re.sub(r"[^a-z0-9]+", "-", key)
    return key.strip("-")


def note_key(it):
    return it.get("arxiv") or normalize_title(it["title"])


def load_note_translations():
    translations = {}
    for code, _, _ in LANGS:
        if code == "ja":
            translations[code] = None
            continue
        path = Path(f"data/i18n/note.{code}.json")
        translations[code] = json.loads(path.read_text()) if path.exists() else {}
    return translations


NOTE_TRANSLATIONS = load_note_translations()


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


def sort_key(it):
    return (-(it.get("citations") or 0), -(it.get("year") or 0))


def anchor(text):
    a = text.lower()
    a = re.sub(r"[^\w\s\-ぁ-んァ-ヶ一-龠ー]", "", a)
    a = a.replace(" ", "-")
    return a


def field_label(field, lang):
    labels = FIELD_I18N.get(field, {})
    return labels.get(lang) or labels.get("ja") or field


def field_heading(field, lang):
    emoji = FIELD_EMOJI.get(field, "•")
    return f"{emoji} {field_label(field, lang)}"


def lang_badges(current):
    badges = []
    for code, filename, autonym in LANGS:
        if code == current:
            badges.append(f"**{autonym}**")
        else:
            badges.append(f"[{autonym}]({filename})")
    return " · ".join(badges)


def note_for(it, lang):
    if lang == "ja":
        return it.get("note") or ""
    return NOTE_TRANSLATIONS.get(lang, {}).get(note_key(it), "")


def fmt_entry(it, lang):
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

    note = note_for(it, lang)
    if note:
        line += f"{STR[lang]['note_separator']}{note}"

    extras = []
    if it.get("github"):
        gh = it["github"]
        star = f"⭐{it['github_stars']}" if it.get("github_stars") is not None else ""
        fm = fresh_marker(it.get("github_pushed"))
        extras.append(f"[`{gh}`](https://github.com/{gh}) {star}{fm}".strip())
    if it.get("page"):
        extras.append(f"[{STR[lang]['project']}]({it['page']})")
    if extras:
        line += " — " + " · ".join(extras)
    return line


def build_by_field(items):
    by_field = defaultdict(lambda: defaultdict(list))
    for it in items:
        by_field[it.get("field", "ai-general")][it.get("subfield", "その他")].append(it)
    ordered_fields = [f for f in FIELD_ORDER if f in by_field] + [f for f in by_field if f not in FIELD_ORDER]
    return ordered_fields, by_field


def render_readme(lang, items, ordered_fields, by_field):
    total = len(items)
    n_gh = sum(1 for it in items if it.get("github"))
    n_fields = len([f for f in by_field])
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    s = STR[lang]

    out = []
    out.append(f"# {s['title']} [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    out.append(f"**{s['lang_label']}:** {lang_badges(lang)}\n")
    out.append(f"> {s['description']}\n")
    out.append(s["summary"].format(total=total, n_fields=n_fields, n_gh=n_gh, today=today) + "\n")
    out.append(s["entry_format"] + "\n")
    out.append(s["legend"] + "\n")
    out.append(s["notes_ref"] + "\n")

    out.append(f"## {s['toc']}\n")
    for field in ordered_fields:
        cnt = sum(len(v) for v in by_field[field].values())
        head = field_heading(field, lang)
        out.append(f"- [{head}](#{anchor(head)}) ({cnt})")
    out.append("")

    for field in ordered_fields:
        out.append(f"## {field_heading(field, lang)}\n")
        for sub in sorted(by_field[field].keys()):
            entries = sorted(by_field[field][sub], key=sort_key)
            out.append(f"### {sub}\n")
            for it in entries:
                out.append(fmt_entry(it, lang))
            out.append("")

    out.append(f"## {s['contribution']}\n")
    out.append(s["contribution_body"] + "\n")
    out.append(f"## {s['license']}\n")
    out.append(s["license_body"] + "\n")
    return "\n".join(out)


def gen_readmes(items, ordered_fields, by_field):
    for code, filename, _ in LANGS:
        Path(filename).write_text(render_readme(code, items, ordered_fields, by_field))


def gen_notes(items, ordered_fields, by_field):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = []
    out.append("# 調査ノート — Awesome AI Survey Papers\n")
    out.append(
        f"本ドキュメントは収集した全サーベイ論文のメタデータ・統計・調査手法をまとめたもの。"
        f"READMEは分類済みリストに徹し、ここに全調査結果を集約する。最終更新 {today}。\n"
    )

    out.append("## 調査手法と飽和判定\n")
    out.append(
        "分野fan-out 並列収集 → 反復波で純増の逓減を観測 → 飽和で終了、という手順を採った"
        "（詳細は [`docs/best-practice.md`](best-practice.md)）。各波は分野クラスタ単位で"
        "複数の収集エージェントを並列起動し、各エージェントが arXiv abs ページの照合・`gh api` による"
        "companion repo 実在確認を経た JSON を出力。親が全 raw をマージ→ arXiv ID/正規化タイトルで"
        "重複排除→ Semantic Scholar batch API で被引用数を付与した。\n"
    )
    out.append("| 波 | 収集テーマ | 重複排除後の累計 | 純増 |")
    out.append("|---|---|---:|---:|")
    out.append("| 第1波 | 主要17分野クラスタ(CV/NLP/LLM/ML/RL/DM・DB・IR/GNN/信頼AI/AI全般 等) | 490 | +490 |")
    out.append("| 第2波 | 薄い分野深掘り・新興ニッチ・GitHubトピック掃き出し・応用横断・知識/DB/DM | 697 | +207 |")
    out.append("| 第3波 | CV深掘り・NLP/古典ML niche・causal/federated/time-series・未収録掃き出し | 889 | +192 |")
    out.append("| 第4波 | 残る薄い分野(tcs/web/hci/ir/evolutionary等)の最終補強・網羅性メタ監査 | 955 | +66 |")
    out.append("")
    out.append(
        "**飽和判定**: 純増が +207 → +192 → +66 と明確に逓減。第4波の網羅性監査では"
        "「必ずあるべき定番サーベイ」の未収録が24件のみで、その大半が2010年代前半の古典層"
        "（最新サーベイは既に高網羅）。rl/knowledge/llm/multimodal/multi-agent/federated/"
        "time-series/recsys 等は探索した定番候補がほぼ全て既収録で飽和に近いと判定された。"
        "**新規の良質サーベイが見つかりにくくなったため、ここで収集を一旦終了する**。\n"
    )
    out.append(
        "**良質な単独サーベイが構造的に乏しいテーマ**（無理に水増しせず明記）: "
        "進化計算の細分(共進化/EDA/メメティック/品質多様性/オープンエンド進化、多くが書籍章や原著)、"
        "TCSのゼロ次最適化・微分可能プログラミング(会議録中心)、HCIのAIフェアネス×ユーザ知覚"
        "(実証研究中心で決定版サーベイ無し)、音声匿名化(手法論文中心)。\n"
    )

    out.append("## 統計\n")
    out.append(f"- 総数: **{len(items)}** 本")
    out.append(f"- 分野数: {len(by_field)}")
    out.append(f"- companion GitHub 付き: {sum(1 for it in items if it.get('github'))} 件")
    out.append(f"- arXiv ID あり: {sum(1 for it in items if it.get('arxiv'))} 件")
    out.append(f"- 被引用数取得済み: {sum(1 for it in items if it.get('citations') is not None)} 件")
    years = Counter(it.get("year") for it in items if it.get("year"))
    out.append("- 出版年の分布: " + ", ".join(f"{y}:{c}" for y, c in sorted(years.items())))
    out.append("")

    out.append("### 分野別件数\n")
    out.append("| 分野 | 件数 | サブ分野数 |")
    out.append("|---|---:|---:|")
    for field in ordered_fields:
        cnt = sum(len(v) for v in by_field[field].values())
        out.append(f"| {field_label(field, 'ja')} | {cnt} | {len(by_field[field])} |")
    out.append("")

    cited = sorted([it for it in items if it.get("citations") is not None], key=lambda x: -x["citations"])[:30]
    if cited:
        out.append("## 被引用数トップ30\n")
        out.append("| 被引用 | タイトル | venue | 年 |")
        out.append("|---:|---|---|---:|")
        for it in cited:
            out.append(f"| {it['citations']} | {it['title'][:70]} | {it.get('venue','')} | {it.get('year','')} |")
        out.append("")

    ghs = sorted([it for it in items if it.get("github")], key=lambda x: -(x.get("github_stars") or 0))
    if ghs:
        out.append("## companion GitHub リポジトリ（star順・実在検証済み）\n")
        out.append("| ⭐star | repo | 最終更新 | 論文 |")
        out.append("|---:|---|---|---|")
        for it in ghs:
            out.append(
                f"| {it.get('github_stars','?')} | "
                f"[{it['github']}](https://github.com/{it['github']}) | "
                f"{(it.get('github_pushed') or '')[:10]} | {it['title'][:50]} |"
            )
        out.append("")

    out.append("## 全エントリ一覧\n")
    for field in ordered_fields:
        out.append(f"### {field_heading(field, 'ja')}\n")
        rows = sorted(by_field_flat(by_field[field]), key=sort_key)
        out.append("| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |")
        out.append("|---|---|---|---:|---|---:|---|")
        for it in rows:
            ax = it.get("arxiv") or ""
            cit = it.get("citations") if it.get("citations") is not None else ""
            gh = it.get("github") or ""
            out.append(
                f"| {it['title'][:60]} | {it.get('authors','')[:25]} | {it.get('venue','')} | "
                f"{it.get('year','')} | {ax} | {cit} | {gh} |"
            )
        out.append("")

    NOTES.write_text("\n".join(out))


def by_field_flat(subdict):
    rows = []
    for values in subdict.values():
        rows.extend(values)
    return rows


def main():
    items = load()
    ordered_fields, by_field = build_by_field(items)
    gen_readmes(items, ordered_fields, by_field)
    gen_notes(items, ordered_fields, by_field)

    n_gh = sum(1 for it in items if it.get("github"))
    print(f"README.md / README.en.md: {len(items)} papers, {len(by_field)} fields, {n_gh} companion repos")
    print("docs/research-notes.md generated")


if __name__ == "__main__":
    main()
