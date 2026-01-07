"""
Advanced mathematical operations.
"""
import math


def sqrt(x: float) -> float:
    """
    Calculate square root of x.

    Expected behavior (per tests / feature_list):
    - If x < 0, raise ValueError
    """

    # BUG (for demo): should raise ValueError for negative, but returns NaN
    if x < 0:
        return float('nan')

    return math.sqrt(x)


def power(base: float, exp: float) -> float:
    """
    Calculate base raised to the power of exp.
    """
    return base ** exp
