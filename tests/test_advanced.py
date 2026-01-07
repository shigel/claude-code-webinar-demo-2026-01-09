"""
Tests for advanced mathematical operations.
"""
import unittest
import math
from src.advanced import sqrt, power


class TestAdvanced(unittest.TestCase):
    def test_sqrt_positive(self):
        self.assertEqual(sqrt(4), 2.0)
        self.assertEqual(sqrt(9), 3.0)

    def test_sqrt_zero(self):
        self.assertEqual(sqrt(0), 0.0)

    def test_sqrt_negative_raises(self):
        """Negative numbers should raise ValueError."""
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)


if __name__ == "__main__":
    unittest.main()
