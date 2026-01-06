---
name: pr-review
description: Performs structured PR reviews with a consistent rubric (correctness, risk, maintainability, tests). Use when reviewing code changes, bugfixes, or before merging.
allowed-tools: Read, Grep, Glob
user-invocable: true
---

# PR Review Skill (Demo)

**必ず日本語で出力すること。**

## 出力形式（Output contract）
必ず以下のセクションを順番に含めること:

1. **要約 (Summary)** - 何が変わったか、なぜ変えたか
2. **Must-fix** - ブロッキング問題（可能な限りファイル/行番号を含める）
3. **リスク / edge cases** - 想定される問題やエッジケース
4. **保守性 (Maintainability)** - 命名、構造、ドキュメント
5. **テスト (Testing)** - 実行したテスト、追加すべきテスト
6. **提案事項 (Suggested follow-ups)** - 任意

## レビュー方針
- 根拠を示す: diff、関数、失敗シナリオを具体的に指摘する
- スタイルの細かい指摘は不要（正確性や保守性に影響する場合のみ）
- 文脈が不足している場合は、前提を明示する

## Rubric
詳細が必要な場合や変更が非自明な場合のみ `checklist.md` を参照する。
