# Claude Code Webinar Demo

Claude Code の **Skills** と **Sub Agents** を段階的に学ぶためのデモリポジトリです。

## 前提

- Python 3.x
- git
- Claude Code（CLI または VSCode拡張）

## このリポジトリの構成

```
main               → 素のClaude Code（何も追加していない状態）
step1-skills       → Skills を追加
step2-subagents-2  → Skills + Sub Agents を追加
```

**ログ付きブランチ（参考用）:**
```
step1-skills-logs     → step1-skills + 実行ログ
step2-subagents-1     → step1-skills + 複数モジュール（並列実行デモ用）
step2-subagents-logs  → step2-subagents-2 + 実行ログ + ウェビナー資料
```

各ブランチは前のブランチの延長です。順番に `git checkout` して違いを体験してください。

**重要:** ブランチを切り替えたら、**Claude Code を再起動**してください。
Skills はセッション起動時にロードされるため、ブランチ切り替え後に再起動しないと新しい Skills が反映されません。
参考: [Agent Skills - Claude Code Docs](https://code.claude.com/docs/en/skills)

---

## main（このブランチ）: 素のClaude Code

**追加ファイル:** なし

このブランチでは Claude Code をそのまま使います。

### できること
- Claude に直接指示してコードを修正
- レビューを依頼

### 課題（次のステップで解決）
- レビュー出力の形式がバラバラ
- 複雑なタスクでコンテキストが膨らむ

### デモ: バグ修正を依頼

```bash
python -m unittest -q  # 1つ失敗する
```

Claude Code を起動:
```
テストが1つ失敗しています。修正してください。
```

### デモ: レビューを依頼

```
src/calculator.py をレビューしてください。
```

→ 出力形式は Claude 任せ（毎回違う可能性あり）

---

## step1-skills: 出力フォーマットを固定する

**追加ファイル:**
```
.claude/skills/pr-review/
├── SKILL.md       # スキル定義
└── checklist.md   # 補足資料
```

### main との違い

| 操作 | main | step1-skills |
|------|------|--------------|
| `/pr-review` | 使えない | 使える |
| レビュー出力 | 形式バラバラ | 6セクション固定 |

### デモ: Skills を使ったレビュー

```bash
git checkout step1-skills
```

Claude Code を起動:
```
/pr-review
```

→ 要約、Must-fix、リスク、保守性、テスト、提案事項の6セクションで固定出力

### Skills とは

- `/スキル名` で呼び出せるカスタムコマンド
- SKILL.md に出力形式や使用ツールを定義
- 毎回同じ観点・形式でタスクを実行

---

## step2-subagents-2: タスクを別プロセスに委譲する

**追加ファイル:**
```
.claude/agents/
├── test-runner.md    # テスト実行・修正の専門エージェント
└── code-reviewer.md  # コードレビューの専門エージェント

.claude/scripts/
├── setup_worktree.sh  # 並列作業用 worktree 作成
└── merge_worktree.sh  # worktree のマージ

CLAUDE.md              # 並列修正の方針
```

### step1 との違い

| 操作 | step1-skills | step2-subagents-2 |
|------|--------------|-------------------|
| バグ修正 | 本体が直接実行 | test-runner に委譲 |
| コンテキスト | 全て本体に蓄積 | Sub Agent 内で完結 |
| 並列実行 | 不可 | 可能（worktree 使用） |

### デモ: Sub Agents を使った並列バグ修正

```bash
git checkout step2-subagents-2
```

Claude Code を起動:
```
バグを全て修正して
```

→ 3つのモジュール（calculator, advanced, formatter）を並列で修正

### Sub Agents とは

- 専門タスクを別プロセスに委譲
- 本体のコンテキストを消費しない
- 結果（成功/失敗、変更内容）だけが返る

---

## まとめ

| 機能 | 解決する課題 | キーファイル |
|------|-------------|-------------|
| Skills | 出力形式のバラつき | `.claude/skills/*/SKILL.md` |
| Sub Agents | コンテキスト肥大化・並列化 | `.claude/agents/*.md` |

---

## 注意

このリポジトリはデモ用です。`src/` 内のモジュールに意図的なバグが含まれています。
