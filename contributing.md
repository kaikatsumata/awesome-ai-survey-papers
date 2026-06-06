# Contributing

本リポジトリは **AI関連分野のサーベイ論文** のキュレーションです。以下の方針に従って貢献してください。

## 掲載基準
- 対象は **サーベイ / レビュー / overview / tutorial 論文** のみ（個別手法の原著論文・モデル本体・ツールは対象外）。
- トップ会議・トップジャーナル・arXiv・正規のプロジェクトページで公開されていること。
- **実在検証**: arXiv ID / DOI / GitHub の実在を確認すること（捏造URL厳禁）。companion repo は実在確認したもののみ。
- 1論文1エントリ。arXiv ID（無ければ正規化タイトル）で重複排除。

## 追加方法（データ駆動）
1. `data/raw/<分野>.json` に以下の形式でエントリを追記:
   ```json
   {
     "title": "...", "authors": "First Author et al.", "venue": "TPAMI",
     "year": 2024, "paper": "https://arxiv.org/abs/XXXX.XXXXX",
     "arxiv": "XXXX.XXXXX", "github": "owner/repo", "page": null,
     "field": "cv", "subfield": "Object Detection", "note": "日本語1行説明"
   }
   ```
2. `python3 data/enrich.py` で検証・メタデータ補強（`data/enriched.json` 生成）。
3. `python3 data/gen.py` で `README.md` と `docs/research-notes.md` を再生成。

`README.md` / `README.en.md` / `docs/research-notes.md` は**自動生成物**なので直接編集しないこと。
READMEは多言語自動生成。翻訳は `data/i18n/note.<lang>.json` に追記してください。

## 品質方針
- 高被引用の定番サーベイと近年の重要サーベイをバランス良く。
- 査読サーベイ・歴史的定番は GitHub の更新が止まっていても掲載価値あり（鮮度ペナルティ免除）。
- 「決定版サーベイが存在しない」テーマは水増しせず、その旨を `docs/research-notes.md` に明記する。
