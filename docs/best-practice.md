# Awesome リスト構築のベストプラクティス（サーベイ論文集 版）

本ドキュメントは、`awesome-ai-survey-papers`（AI分野のサーベイ論文キュレーション）を
構築した経験に基づく再利用可能な指針。一般的作法は `~/awesome-awesome/docs/best-practices.md`
（リストのリスト版）を継承し、ここでは**「論文そのものを集める awesome リスト」特有の学び**を追記する。

---

## 1. 「論文集」awesome 特有のデータモデル

「リストのリスト」と違い、対象が**個別の論文**になると1エントリの構成要素が増える:

- `title` / `authors`（筆頭 + et al.）/ `venue` / `year`
- `paper`（一次URL: arXiv abs か DOI）/ `arxiv`（ID）
- `github`（companion / 論文リスト リポジトリ、任意）/ `page`（プロジェクトページ、任意）
- `citations`（被引用数）/ `field` / `subfield` / `note`（1行説明）

**正規化キー**は arXiv ID を第一に使う（無ければ正規化タイトル）。会議版とarXiv版の二重掲載を防げる。

---

## 2. 実在検証のための具体的ノウハウ（重要）

### arXiv API は環境によって 429 で詰まる → abs ページの WebFetch が確実
- `http://export.arxiv.org/api/query?id_list=ID` はIP単位のレート制限で **継続的に HTTP 429** を返すことがある。
  本セッションでは全エージェントが429に当たった。
- 回避策: **`https://arxiv.org/abs/<ID>` を WebFetch** し、HTMLメタ（`citation_title`/`citation_author`/`citation_date`）で
  タイトル・筆頭著者・年を照合する。これが最も安定。`curl` が HTTP/2 でハングする環境もあるため WebFetch 推奨。
- それも不確実なら **WebSearch でタイトル＋arXiv IDを照合**。

### 被引用数は Semantic Scholar の batch API が効率的
- `POST https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,year,venue`
  に `{"ids":["ARXIV:2103.00001", ...]}`（最大500件/リクエスト）を投げると一括取得できる。
  本セッションでは 490件中 475件（97%）の被引用数を取得できた。
- 並び順（重要度順）の主軸として被引用数を使えるので、収集後に必ず付与する価値がある。

### companion GitHub は必ず `gh api` で実在確認
- `gh api repos/owner/repo --jq .full_name` で正規名・star・`pushed_at`・`archived` を取得。
- **404 のものは捏造として除去**（エージェントは存在しないcompanionを推測しがち）。casing差は正規名に補正。

---

## 3. 「サーベイ論文」と「原著（手法）論文」を峻別する

- 収集エージェントは、定番だからと **landmark な原著論文**（例: Attention Is All You Need, Mamba, KAN,
  Lottery Ticket, BatchNorm）を混入させがち。本リポジトリの対象は **survey / review / overview / tutorial** に限る。
- 対策: プロンプトで「サーベイのみ」と明示し、タイトルに `Survey` / `Review` / `A Comprehensive ...` 等を
  含むかを目安にする。原著を入れる場合は別カテゴリ（"基礎参照"）として明示し、混ぜない。
- 例外: その分野の**起点となった提唱論文**（learned index の Kraska 論文など）は文脈上有用なら
  注記付きで残す判断もあるが、原則は分離。

---

## 4. 分野fan-out 並列収集 + マージ/重複排除パイプライン

- **分野クラスタ単位**（CV / NLP+音声 / LLM+生成 / ML+理論 / RL+ロボ / DM+DB+IR / GNN+知識 / 信頼AI+他）で
  エージェントを並列起動し、各々が `data/raw/<cluster>.json` に検証済みJSON配列を書く。
- 親（オーケストレータ）は `enrich.py` で **全 raw をマージ → arXiv/タイトルで重複排除 → API補強** する。
- 本セッションの実績: 8クラスタ並列で **538件 → 重複排除490件**（クロス重複は約9%）。
  分野横断のトピック（拡散モデル、知識グラフ×LLM等）は複数エージェントが拾うため重複は必ず出る。
  → **重複は気にせず集めさせ、パイプラインで吸収**する設計が効率的。

## 5. 波（wave）で逓減を観測し飽和で止める

- 第1波: 主要分野を広く（→490件）。第2波: 薄い分野の深掘り + 新興ニッチ + GitHubトピック掃き出し +
  応用横断。第3波以降: さらに細分・飽和確認。
- 各波の新規追加数（重複排除後の純増）が逓減し、主要分野に大きな抜けが無くなったら終了。

## 6. 運用上の落とし穴

- **セッション利用上限**: 大量の並列エージェントは利用上限に達することがある。上限に当たると
  エージェントは**ファイル書き込み前に停止し成果ゼロ**になりうる。波を分割し、各波完了後に
  `enrich.py`/`gen.py` を回して**こまめにコミット**するのが安全。
- **READMEと調査ノートの分離**: READMEは分類済みリストに徹し、全メタデータ・統計・全エントリ表は
  `docs/research-notes.md` に置く（自動生成）。手編集せずスクリプト再実行で更新。
- **鮮度マーカーの例外**: サーベイの companion リポジトリは更新が止まっていても網羅性・権威性で価値が高い。
  🔴でも掲載し、その旨を凡例に明記する。

---

## チェックリスト（論文集 awesome 版）

- [ ] 1エントリに title/authors/venue/year/paper/arxiv/github/page/citations/field/subfield/note
- [ ] arXiv ID を正規化キーに重複排除（abs ページ WebFetch で実在検証）
- [ ] 被引用数を Semantic Scholar batch API で付与し、重要度順の主軸にする
- [ ] companion GitHub は `gh api` で実在確認、404は除去
- [ ] **サーベイ論文と原著論文を峻別**（原著の混入を弾く）
- [ ] 分野fan-out 並列 → マージ/重複排除パイプライン → こまめにコミット
- [ ] 波で逓減観測 → 飽和で終了
- [ ] README（分類リスト）と research-notes（全調査結果）を分離・自動生成
