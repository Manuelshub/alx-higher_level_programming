#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the function that returns the max of
        numbers in a list.
    """
    def test_max_integer(self):
        """Testing the function max_integer."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([7, 45, 23, 65]), 65)
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
