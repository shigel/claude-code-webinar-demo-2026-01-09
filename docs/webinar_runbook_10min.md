# Claude Code Webinar Runbook (10分30秒版)
目的: “全部” を説明しない。SubagentsとSkillsを体感させ、Harnessは概念だけ残す。

## 0:00–1:00 イントロ
- 3つの違いを1枚で言い切る（細部は捨てる）

## 1:00–6:30 デモ（Subagents中心）
- failing test を見せる → test-runner subagent で直す → テスト通過が証拠
- 余裕があれば code-reviewer subagent でレビュー

## 6:30–9:30 Skills（1分で要点だけ）
- SKILL.md の description がトリガ
- allowed-tools で read-only もできる
- SubagentはSkill継承しない → skills: で明示（ここだけ刺す）

## 9:30–10:30 Harness（概念だけ）
- claude-progress / feature_list / init.sh の3点セットを “写真で” 見せる
- 詳細は20分版で、または資料リンクで
