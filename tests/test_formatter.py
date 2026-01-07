"""
Tests for output formatting utilities.
"""
import unittest
from src.formatter import format_number, format_result


class TestFormatter(unittest.TestCase):
    def test_format_number_default(self):
        self.assertEqual(format_number(3.14159), "3.14")

    def test_format_number_custom_decimals(self):
        """Should respect the decimals parameter."""
        self.assertEqual(format_number(3.14159, decimals=4), "3.1416")
        self.assertEqual(format_number(3.14159, decimals=0), "3")

    def test_format_result(self):
        result = format_result("+", 2, 3, 5)
        self.assertEqual(result, "2 + 3 = 5")


if __name__ == "__main__":
    unittest.main()
