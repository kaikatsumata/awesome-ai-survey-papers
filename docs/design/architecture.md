# Awesome AI Survey Papers — 設計

## 目的
研究サーベイにおいて良質な情報を提供する。AI関連分野のトップ会議・トップジャーナル・arXiv・
個人/プロジェクトサイトで公開・出版された**サーベイ論文（survey / review / overview）そのもの**を
収集・分類・キュレーションする。

`awesome-awesome`（リストのリスト）とは異なり、本リポジトリの一次対象は**サーベイ論文**である。

## 収集対象（1エントリの構成要素）
- `title`: 論文タイトル
- `authors`: 著者（代表 + et al.）
- `venue`: 出版先（会議略称 / ジャーナル名 / arXiv）
- `year`: 出版年
- `paper`: 論文URL（arXiv abs / DOI / PDF）。一次リンク
- `arxiv`: arXiv ID（あれば）
- `github`: companion / 論文リスト リポジトリ（あれば）
- `page`: プロジェクト/個人ページ（あれば）
- `citations`: 被引用数（Semantic Scholar、取得できれば）
- `field` / `subfield`: 分野分類
- `note`: 1行説明（何のサーベイか）

## 分野分類（taxonomy）
ユーザ指定の会議分野を内包しつつ、サーベイが多い「研究テーマ」軸で整理する。
ML / 学習理論 / 理論計算機科学 / ニューラルネット / AI全般 / データマイニング / DB /
CV / NLP / 音声 / 情報検索 / HCI / WWW / 進化計算 / マルチエージェント / 知識表現 /
推薦・クラウドソーシング、および追加: LLM / 生成AI・拡散 / マルチモーダル / GNN /
強化学習 / ロボティクス / AI安全性・アライメント / 公平性・説明可能性 / 連合学習 /
因果推論 / 時系列 / AI for Science / グラフ / 自己教師あり / 効率化（量子化・蒸留）等。

## パイプライン（データ駆動）
1. `data/surveys.json` … 出典（手動キュレーション + エージェント収集をマージ）
2. `data/enrich.py` … arXiv API / Semantic Scholar API / GitHub API でメタデータ補強・実在検証
   → `data/enriched.json`
3. `data/gen.py` … `enriched.json` から `README.md`（分類済みリスト）と
   `docs/research-notes.md`（全調査結果・統計）を生成
4. GitHub Actions (cron) で被引用数・companion repo の鮮度を定期更新

## 品質方針（best-practices.md 準拠）
- 査読サーベイ(📑)・歴史的定番(📚)は鮮度ペナルティ免除
- 正規URL/正規IDで重複排除
- READMEは分類済み一覧、調査ノートは別ドキュメント
- 捏造URLを排除、実在検証（arXiv/DOI/GitHub）を必須化
- 「決定版サーベイが存在しない」テーマは水増しせず明記

## 調査手法
(A) 分野fan-out 並列収集 → (B) 反復波で逓減観測・飽和判定 →
(C) arXiv `cs.*` のsurveyクエリ掃き出し → (D) prolific著者/サーベイ常連グループ深掘り →
(E) 「X: A Survey」パターン狙い撃ち → (F) 実在検証と誠実な報告
