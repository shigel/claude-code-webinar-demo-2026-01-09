---
name: pr-review
description: Performs structured PR reviews with a consistent rubric (correctness, risk, maintainability, tests). Use when reviewing code changes, bugfixes, or before merging.
allowed-tools: Read, Grep, Glob
---

# PR Review Skill (Demo)

## Output contract
Always respond with these sections, in order:

1. **Summary** (what changed, why)
2. **Must-fix** (blocking issues; include file/line pointers when possible)
3. **Risks / edge cases**
4. **Maintainability** (naming, structure, docs)
5. **Testing** (what was run, what should be added)
6. **Suggested follow-ups** (optional)

## Review method
- Prefer evidence: point to diffs, functions, or failing scenarios.
- Do not nitpick style unless it impacts correctness or maintenance.
- If context is missing, state assumptions explicitly.

## Rubric
Read `checklist.md` only when you need deeper detail or if the change is non-trivial.
