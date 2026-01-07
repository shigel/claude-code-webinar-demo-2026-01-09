"""
Output formatting utilities.
"""


def format_number(value: float, decimals: int = 2) -> str:
    """
    Format a number with specified decimal places.

    Expected behavior (per tests / feature_list):
    - Return string with exactly 'decimals' decimal places
    """

    # BUG (for demo): ignores decimals parameter, always uses 2
    return f"{value:.2f}"


def format_result(operation: str, a: float, b: float, result: float) -> str:
    """
    Format a calculation result as a readable string.
    """
    return f"{a} {operation} {b} = {result}"
