#!/usr/bin/env bash
# GitHub リポジトリに Topics(タグ)を設定する。
#
# 使い方:
#   ./scripts/set-topics.sh             # origin のリポジトリに設定
#   ./scripts/set-topics.sh owner/repo  # リポジトリを明示
#
# 前提: gh CLI が認証済み。GitHub の制約: 最大20件、英小文字・数字・ハイフンのみ。
set -euo pipefail

cd "$(dirname "$0")/.."

repo_arg=()
if [[ $# -ge 1 ]]; then
  repo_arg=("$1")
fi

gh repo edit "${repo_arg[@]}" \
  --add-topic awesome \
  --add-topic awesome-list \
  --add-topic awesome-lists \
  --add-topic survey \
  --add-topic survey-papers \
  --add-topic paper-list \
  --add-topic papers \
  --add-topic artificial-intelligence \
  --add-topic machine-learning \
  --add-topic deep-learning \
  --add-topic computer-vision \
  --add-topic nlp \
  --add-topic large-language-models \
  --add-topic reinforcement-learning \
  --add-topic generative-ai \
  --add-topic multimodal \
  --add-topic graph-neural-networks \
  --add-topic ai-research \
  --add-topic curated-list \
  --add-topic resources

echo "Topics を設定しました: ${1:-origin repository}"
