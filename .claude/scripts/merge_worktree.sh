#!/bin/bash
# Usage: ./.claude/scripts/merge_worktree.sh <module-name>
# 指定されたモジュールの worktree をマージしてクリーンアップする

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <module-name>"
    echo "Example: $0 calculator"
    exit 1
fi

MODULE="$1"

# モジュール名にマッチする worktree を検索
WORKTREE_PATH=$(find .worktrees -maxdepth 1 -type d -name "${MODULE}-*" 2>/dev/null | head -1)

if [ -z "$WORKTREE_PATH" ]; then
    echo "Error: No worktree found for module '$MODULE'"
    echo "Available worktrees:"
    ls -1 .worktrees/ 2>/dev/null || echo "  (none)"
    exit 1
fi

# ブランチ名を取得
BRANCH_NAME=$(git -C "$WORKTREE_PATH" rev-parse --abbrev-ref HEAD)

echo "Merging worktree: $WORKTREE_PATH"
echo "Branch: $BRANCH_NAME"

# 現在のブランチにマージ
git merge "$BRANCH_NAME" --no-edit

# worktree を削除
git worktree remove "$WORKTREE_PATH"

# ブランチを削除
git branch -d "$BRANCH_NAME"

echo ""
echo "✓ Merged and cleaned up: $MODULE"
