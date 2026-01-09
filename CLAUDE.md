# Claude Code デモプロジェクト

## バグ修正の方針

複数モジュールにバグがある場合は、**並列で修正**すること。

### 手順

1. 各モジュールごとに worktree を作成:
   ```bash
   .claude/scripts/setup_worktree.sh <module-name>
   ```

2. 各モジュールに対して **test-runner を並列起動**:
   - 作業ディレクトリとして `.worktrees/<module-name>` を指定
   - 例: calculator-${date +%Y%m%d-%H%M%S}, advanced-${date +%Y%m%d-%H%M%S}, formatter-${date +%Y%m%d-%H%M%S} を同時に修正

3. 完了後、必要に応じてマージ:
   ```bash
   .claude/scripts/merge_worktree.sh <module-name>
   ```

### 例

```
ユーザー: 「バグを全て修正して」

→ 失敗しているテストを確認
→ 各モジュールごとに setup_worktree.sh 実行
→ test-runner を並列起動（各 worktree を指定）
→ 必要に応じて merge_worktree.sh で統合
```

## テスト実行

```bash
python -m unittest -q
```
