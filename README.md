# Claude Code Webinar Demo

Claude Code の **skills / subagents / harness** を段階的に学ぶためのデモリポジトリです。

## 前提

- Python 3.x
- git
- Claude Code（CLI または VSCode拡張）

## このリポジトリの構成

```
main            → 素のClaude Code（何も追加していない状態）
step1-skills    → skills を追加
step2-subagents → skills + subagents を追加
step3-harness   → skills + subagents + harness（全部入り）
```

各ブランチは前のブランチの延長です。順番に `git checkout` して違いを体験してください。

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
- セッションが途切れると作業状態を失う

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

### デモ: skills を使ったレビュー

```bash
git checkout step1-skills
```

Claude Code を起動:
```
/pr-review
```

→ 要約、Must-fix、リスク、保守性、テスト、提案事項の6セクションで固定出力

### skills とは

- `/スキル名` で呼び出せるカスタムコマンド
- SKILL.md に出力形式や使用ツールを定義
- 毎回同じ観点・形式でタスクを実行

---

## step2-subagents: タスクを別プロセスに委譲する

**追加ファイル:**
```
.claude/agents/
├── test-runner.md    # テスト実行・修正の専門エージェント
└── code-reviewer.md  # コードレビューの専門エージェント
```

### step1 との違い

| 操作 | step1-skills | step2-subagents |
|------|--------------|-----------------|
| バグ修正 | 本体が直接実行 | test-runner に委譲 |
| コンテキスト | 全て本体に蓄積 | subagent 内で完結 |

### デモ: subagents を使ったバグ修正

```bash
git checkout step2-subagents
```

Claude Code を起動:
```
test-runner subagent を使って、失敗しているテストを修正してください。
```

→ test-runner が テスト実行→解析→修正→再実行 を自律的に行い、結果だけ返す

### subagents とは

- 専門タスクを別プロセスに委譲
- 本体のコンテキストを消費しない
- 結果（成功/失敗、変更内容）だけが返る

---

## step3-harness: セッションをまたいで状態を維持する

**追加ファイル:**
```
CLAUDE.md           # 運用ルール（毎回Claudeが読む）
init.sh             # セッション開始時のスモークテスト
feature_list.json   # 機能の進捗管理
claude-progress.txt # 引き継ぎログ
```

### step2 との違い

| 操作 | step2-subagents | step3-harness |
|------|-----------------|---------------|
| セッション開始 | 毎回ゼロから | init.sh で状態確認 |
| 作業状態 | 途切れると失う | claude-progress.txt で引き継ぎ |
| 進捗管理 | なし | feature_list.json で追跡 |

### デモ: harness を使った継続作業

```bash
git checkout step3-harness
```

Claude Code を起動（セッション1回目）:
```
CLAUDE.md を読んで、セッション開始ルーチンを実行してください。
```

→ init.sh 実行、feature_list.json 確認、作業開始

セッションを終了し、新しいセッションを開始（2回目）:
```
前回の続きをお願いします。
```

→ claude-progress.txt を読んで、前回の作業を把握して継続

### harness とは

- セッションをまたいでも破綻しない仕組み
- CLAUDE.md で運用ルールを固定
- 進捗と引き継ぎを明示的に管理

---

## まとめ

| 機能 | 解決する課題 | キーファイル |
|------|-------------|-------------|
| skills | 出力形式のバラつき | `.claude/skills/*/SKILL.md` |
| subagents | コンテキスト肥大化 | `.claude/agents/*.md` |
| harness | セッション断絶 | `CLAUDE.md`, `feature_list.json`, `claude-progress.txt` |

---

## 注意

このリポジトリはデモ用です。`src/calculator.py` に意図的なバグが含まれています。
