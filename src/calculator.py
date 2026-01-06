"""Simple calculator module (intentionally contains a bug for demo)."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Expected behavior (per tests / feature_list):
    - If b == 0, raise ValueError
    """

    # BUG (for demo): should raise, but returns 0
    if b == 0:
        return 0

    return a / b
