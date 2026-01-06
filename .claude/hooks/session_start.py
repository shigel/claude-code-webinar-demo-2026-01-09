#!/usr/bin/env python3
import json
import os
import pathlib

PROJECT_DIR = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")).resolve()

def read_text(path: pathlib.Path, max_bytes: int = 12000) -> str:
    if not path.exists():
        return ""
    data = path.read_bytes()[:max_bytes]
    try:
        return data.decode("utf-8", errors="replace")
    except Exception:
        return data.decode(errors="replace")

def main() -> int:
    progress = read_text(PROJECT_DIR / "claude-progress.txt")
    feature_list_path = PROJECT_DIR / "feature_list.json"
    failing = []
    if feature_list_path.exists():
        try:
            fl = json.loads(read_text(feature_list_path))
            for item in fl:
                if not item.get("passes", False):
                    failing.append(item.get("description", ""))
        except Exception:
            pass

    ctx_lines = []
    ctx_lines.append("[Harness] SessionStart context loaded.")
    if progress:
        tail = "\n".join(progress.strip().splitlines()[-12:])
        ctx_lines.append("\n[claude-progress.txt tail]\n" + tail)
    if failing:
        ctx_lines.append("\n[Next failing features]\n- " + "\n- ".join(failing[:5]))
    else:
        ctx_lines.append("\n[Next failing features]\n(none detected)")

    out = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "\n".join(ctx_lines)
        }
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
