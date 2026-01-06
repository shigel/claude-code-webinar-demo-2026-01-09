#!/usr/bin/env python3
"""PostToolUse hook: run unit tests after edits/writes; if failing, force Claude to fix."""
import json
import subprocess
import sys

def run_tests() -> tuple[int, str]:
    try:
        p = subprocess.run(
            [sys.executable, "-m", "unittest", "-q"],
            capture_output=True,
            text=True,
            check=False,
        )
        out = (p.stdout or "") + (p.stderr or "")
        return p.returncode, out.strip()
    except Exception as e:
        return 1, f"Failed to run tests: {e}"

def main() -> int:
    # Consume hook input JSON from stdin (not used, but required to avoid broken pipe in some environments)
    try:
        _ = json.load(sys.stdin)
    except Exception:
        pass

    code, out = run_tests()
    if code == 0:
        # Nothing to do.
        return 0

    payload = {
        "decision": "block",
        "reason": "Unit tests are failing. Fix the failures before continuing.",
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": f"[unittest output]\n{out[:4000]}"
        }
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
