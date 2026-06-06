#!/usr/bin/env bash
# データ補強 → 多言語README/調査ノート再生成 を一括実行
set -e
cd "$(dirname "$0")/.."
python3 data/enrich.py
python3 data/gen.py
echo "refresh done."
