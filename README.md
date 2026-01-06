# Claude Code Webinar Demo Repo (Subagents / Skills / Harness)

このリポジトリは、勉強会/ウェビナーで **Claude Code の Subagents / Skills / Harness** を 1つの流れでデモするための最小構成です。

## 目的（このrepoで見せること）
1. **Subagent** に「テスト実行・失敗解析・修正」を委譲して、本線のコンテキストを汚さない
2. **Skill**（pr-review）でレビュー観点を標準化し、出力を安定させる
3. **Harness**（feature_list.json + claude-progress.txt + init.sh + CLAUDE.md）で長時間/多セッションでも破綻しない

## 前提
- Python 3.x
- git
- Claude Code が動く環境（CLI）

## まずはローカルでテストが落ちることを確認
```bash
python -m unittest -q
```
`divide` の仕様が不正なので、1つ落ちます（デモでClaudeに直させる想定）。

## Claude Code デモ（コピペ用）
Claude Code をリポジトリ直下で起動して、以下を入力してください。

### 1) バグ修正（Subagent）
```text
いま failing な unit test を直して。
- test-runner subagent を使って、テスト実行→失敗解析→最小修正→再実行までやって。
- 修正が終わったら feature_list.json の該当項目の passes を true にして（passes 以外の編集は禁止）。
- 最後に claude-progress.txt に「やったこと/次にやること」を追記して。
```

### 2) 変更レビュー（Skill + Subagent）
```text
直した変更点を code-reviewer subagent にレビューさせて（pr-review Skill を使う前提で）。
追加で、テスト観点で不安があれば指摘して。
```

## 重要なファイル
- `CLAUDE.md` : セッション開始時にClaudeが読む “運用ルール”
- `feature_list.json` : E2E/受け入れ観点のリスト（harnessの背骨）
- `claude-progress.txt` : セッションまたぎの引き継ぎ（harnessの背骨）
- `init.sh` : 毎セッションの “最初にやること” を固定化
- `.claude/agents/*` : Subagents 定義
- `.claude/skills/*` : Skills 定義
- `.claude/settings.json` : Hooks（任意：デモで見せるなら使う）

## 注意
このrepoは “デモ用に意図的に不具合を含む” 状態です。本番コードにそのまま流用しないでください。
