# Claude Code: Skills と Sub Agents

**CNX×najiminoプレゼンツ [AI駆動開発] 実開発ウェビナー 第3回**

2026年1月9日（金）19:00〜

イベントページ: https://lu.ma/0jnm9k2o

---

## 自己紹介

### 斉藤 滋（さいとう しげる）

- najimino 代表取締役
- AI駆動開発の実践・研究
- Claude Code ヘビーユーザー

---

## 今日のゴール

1. Claude Code の全体像を「組織」で理解
2. **Skills** と **Sub Agents** の違いを説明できる
3. デモで動作を確認

---

## 背景: AI駆動開発の今

---

### 役割の変化

| 従来 | AI駆動開発 |
|------|-----------|
| PM: 要件定義・進捗管理 | PM: + AIへの指示・レビュー |
| 開発者: 設計・実装・テスト | 開発者: + AIへの指示・レビュー |
| - | AI: 実装・テスト・ドキュメント |

---

### 起きていること

- 開発者の定型作業 → AI が担当
- PM の作業増加 → AI への指示・レビュー
- **役割の重複** → 「AI への指示」が共通タスクに

---

### 課題

- 非エンジニアも AI ツールを理解する必要
- 「AI に何をどう任せるか」の設計が重要

→ **Claude Code を「組織」に例えて理解する**

---

## Claude Code = 開発チーム

---

### 全体像

```
┌──────────────────────────────────────────┐
│            経営・PM層                     │
│  CLAUDE.md = 会社の方針・ルール           │
│  Settings = ガバナンス・権限              │
│  Harness = 長期PJの進捗管理               │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│      Claude Code = 開発責任者             │
│  依頼を受け、判断・実行・委譲             │
└──────────────────────────────────────────┘
         ↓              ↓              ↓
┌────────────┐  ┌────────────┐  ┌────────────┐
│ Sub Agent  │  │ Sub Agent  │  │ Sub Agent  │
│ = 部下     │  │ = 部下     │  │ = 部下     │
│ test-runner│  │code-reviewer│ │  explore   │
└────────────┘  └────────────┘  └────────────┘
         ↓              ↓              ↓
┌──────────────────────────────────────────┐
│       Skills = 専門知識・手順書           │
│  pr-review / security-check など         │
└──────────────────────────────────────────┘
```

---

### 対応表

| 概念 | 組織での例え |
|------|-------------|
| Claude Code 本体 | 開発責任者 |
| Sub Agents | 部下（専門チーム） |
| Skills | 専門知識・手順書 |
| CLAUDE.md | 会社の方針 |
| Hooks | 自動チェック |

---

## 今日の話

```
┌──────────────────────────────────────────┐
│  CLAUDE.md / Settings / Harness / Hooks  │
│  → 第4回で詳しく                          │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│  ★ 今日のテーマ ★                        │
│                                          │
│  Sub Agents（部下）                       │
│  Skills（専門知識）                       │
└──────────────────────────────────────────┘
```

---

### 2つの概念

| 概念 | 例え | 説明 |
|------|------|------|
| Sub Agents | 部下に任せる | 別コンテキストで並行処理 |
| Skills | マニュアル参照 | 必要時だけ知識をロード |

---

## 1. Skills（専門知識）

---

### Skills とは

- 「やり方」を教える Markdown
- 必要な時だけ自動で読み込む
- 全部暗記させる必要なし

---

### ディレクトリ構造

```
.claude/skills/
  pr-review/
    SKILL.md         # スキル定義
    checklist.md     # 詳細リスト
```

---

### SKILL.md の例（デモ環境）

```yaml
---
name: pr-review
description: PRレビューを実施。コード変更の
             レビュー依頼時に使用。
allowed-tools: Read, Grep, Glob, Bash
---

# PR Review

## チェック観点
1. 正確性: 要件とテストに沿っているか
2. リスク: エッジケース、セキュリティ
3. 保守性: 可読性、命名

## 出力形式
- サマリー
- 必須修正 / 推奨 / nice-to-have
```

---

## 2. Sub Agents（部下）

---

### Sub Agents とは

- 専門チームに仕事を振る
- 独立して作業、結果を報告
- 本線のコンテキストを汚さない

---

### 設定例（デモ環境）

```yaml
---
name: test-runner
description: テストを実行し、失敗を診断・修正。
             worktreeでの並列作業に使用。
tools: Read, Grep, Glob, Bash, Edit, Write
model: sonnet
---

テスト自動化の専門家として作業します。

## ワークフロー
1) テスト実行
2) 失敗の原因特定
3) 最小の修正
4) 再テストで確認
5) 報告
```

---

### 委譲パターン

| パターン | 担当 |
|----------|------|
| レビュー | code-reviewer |
| テスト | test-runner |
| 調査 | explore |

---

## 3. Skills × Sub Agents

---

### 重要: 継承しない

Sub Agents はメイン会話の Skills を **自動継承しない**

→ `skills:` で明示して渡す

---

### 接続例

```yaml
---
name: code-reviewer
description: コード変更をレビュー。
tools: Read, Grep, Glob
skills: pr-review    # ← 明示
---
```

---

## デモ

**IDE から Claude Code を起動して実行**

---

### デモ 1: Skills

`/pr-review` でPRレビューを実行

---

### デモ 2: Sub Agents

「不具合を修正して」で並列バグ修正

- 3つのモジュールを同時に修正
- 各モジュールで独立したブランチ

---

### デモ結果（参考）

```
⏺ 3 test-runner agents finished
  ├─ calculator · 6 tool uses · 9.6k tokens
  ├─ advanced   · 6 tool uses · 9.6k tokens
  └─ formatter  · 6 tool uses · 9.7k tokens

✻ 1m 17s
```

---

## まとめ

| 概念 | 用途 |
|------|------|
| Skills | 専門知識を必要時にロード |
| Sub Agents | 並列処理・コンテキスト分離 |

**組み合わせて使う**: Sub Agent に Skills を渡す

---

## デモリポジトリ

**GitHub**: https://github.com/shigel/claude-code-webinar-demo-2026-01-09

### ブランチ構成

| ブランチ | 内容 |
|----------|------|
| main | 空（スタート地点） |
| step1-skills | Skills 追加 |
| step2-subagents-2 | Sub Agents 追加 |
| step2-subagents-logs | 実行ログ付き |

---

# お知らせ

---

## 第4回 ウェビナー予告

**Claude Code を"本番運用レベル"で回すためのハーネス（仮）**

- 日時: 2026年2月4日（水）19:00〜
- 内容: Harness / Hooks / CLAUDE.md / Settings

イベントページ: https://lu.ma/3pu7631g

**登壇者募集中！** LT枠（5分×2）あります

---

## アンケートのお願い

**興味のある項目にチェックしてください**

| 項目 | 内容 |
|------|------|
| 次回ウェビナー | 第4回（2/4）のご案内 |
| najimino交流所 | AI活用の情報交換 Slack |
| AI受託開発 | 導入支援・PoC・設計 |
| エンジニア募集 | PM / バックエンド / AI |

→ **アンケートにチェックいただいた方に個別連絡**

（アンケートURL）

---

## ご清聴ありがとうございました

---

# 付録

---

## A. Skills デモログ

### Skills あり（/pr-review 実行時）

```
> The "pr-review" skill is running

⏺ PR レビューを開始します。現在のブランチと
  ステージング済みの変更を確認します。

⏺ Bash(git status)
⏺ Bash(git diff --cached)
⏺ Read(.claude/skills/pr-review/SKILL.md)

⏺ PRレビュー結果

  1. 要約 (Summary)
  2. Must-fix
  3. リスク / edge cases
  4. 保守性 (Maintainability)
  5. テスト (Testing)
  6. 提案事項 (Suggested follow-ups)
```

**特徴**: 6セクション固定、スキル起動表示あり

---

### Skills なし（通常のレビュー依頼）

```
⏺ PRのレビューを行います。まず変更内容を確認します。

⏺ Bash(git diff)

⏺ このPRに対してどのようなレビューを希望しますか？
  - セキュリティ重視
  - パフォーマンス重視
  - 一般的なコードレビュー

（ユーザー応答後）

⏺ レビュー結果
  - 概要
  - 問題点
  - 改善提案
  ...
```

**特徴**: セクション構成がバラバラ、質問が発生

---

## B. Sub Agents デモログ

### 修正内容

| モジュール | 問題 | 修正 |
|------------|------|------|
| calculator | ゼロ除算で return 0 | raise ValueError |
| advanced | 負の数で NaN | raise ValueError |
| formatter | decimals 無視 | パラメータ反映 |

### 比較

| 項目 | With Sub Agents | Without |
|------|-----------------|---------|
| 時間 | 1m 17s | 53s |
| 並列 | 3同時 | 順次 |
| 分離 | 3ブランチ | 直接編集 |

---

## C. 参考資料

### 公式ドキュメント

- [Sub Agents](https://code.claude.com/docs/en/sub-agents)
- [Skills](https://code.claude.com/docs/en/skills)
- [Hooks](https://code.claude.com/docs/en/hooks-guide)

### デモリポジトリ

https://github.com/shigel/claude-code-webinar-demo-2026-01-09
