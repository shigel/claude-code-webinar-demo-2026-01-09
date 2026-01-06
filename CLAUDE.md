# Claude Code Webinar Demo: Operating Rules (Harness)

あなたはこのリポジトリの「作業者」です。セッションが途切れても破綻しないように、必ず次を守ってください。

## 0) セッション開始のルーチン（毎回）
1. `claude-progress.txt` を読む（直近の作業と次の一手を把握）
2. `feature_list.json` を読む（未完了の feature を1つだけ選ぶ）
3. `./init.sh` を実行して、現状が壊れていないか最小の smoke を通す

## 1) 進め方（1セッション = 1機能）
- 1回のセッションでは **feature_list.json の passes:false の項目を 1つだけ** true にする
- 途中で終わりそうなら “手を広げず”、未完了のままでも **claude-progress.txt に明確に残す**
- 最後に必ずユニットテストを通す（`python -m unittest -q`）

## 2) feature_list.json の編集ルール（重要）
- **変更してよいのは passes フィールドだけ**
- description/steps/category の書き換え、行の削除、順序変更は禁止

## 3) セッション終了時（毎回）
- 何をしたか / 何が残っているか / 次にやること を `claude-progress.txt` に追記する
- 可能なら git commit して区切る（デモでは任意）

## 4) Subagents
- テストは `test-runner` に任せる
- レビューは `code-reviewer` に任せる（pr-review Skill を使う）
