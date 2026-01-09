#!/bin/bash
# Usage: ./.claude/scripts/setup_worktree.sh <module-name>
# 指定されたモジュール用の worktree を .worktrees/ 内に作成する

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <module-name>"
    echo "Example: $0 calculator"
    exit 1
fi

MODULE="$1"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
WORKTREE_NAME="${MODULE}-${TIMESTAMP}"
WORKTREE_PATH=".worktrees/${WORKTREE_NAME}"
BRANCH_NAME="fix-${MODULE}-${TIMESTAMP}"

# .worktrees ディレクトリがなければ作成
mkdir -p .worktrees

# 古い worktree 参照をクリーンアップ
git worktree prune 2>/dev/null || true

# 新しいブランチで worktree を作成
git worktree add -b "$BRANCH_NAME" "$WORKTREE_PATH"

echo "✓ Worktree created: $WORKTREE_PATH"
echo "✓ Branch: $BRANCH_NAME"
echo ""
echo "To work in this worktree:"
echo "  cd $WORKTREE_PATH"
