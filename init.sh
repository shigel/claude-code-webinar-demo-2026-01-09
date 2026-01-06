#!/usr/bin/env bash
set -euo pipefail

echo "[init] python version:"
python --version

echo "[init] running unit tests (smoke)..."
python -m unittest -q
echo "[init] OK"
