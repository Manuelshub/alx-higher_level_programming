#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the function that returns the max of
        numbers in a list.
    """
    def test_positive_ints(self):
        """Testing the function with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([7, 45, 23, 65]), 65)

    def test_empty_list(self):
        """Testing the function with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        """Testing the function with a string."""
        self.assertEqual(max_integer("Hello"), 'o')

    def test_empty_string(self):
        """Testing the function with an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_single_element(self):
        """Testing the function with a single element."""
        self.assertEqual(max_integer([10]), 10)

    def test_string_list(self):
        """Testing the function with a list of string."""
        self.assertEqual(max_integer(["Hello", "World"]), "World")

    def test_negative_ints(self):
        """Testing the function with negative integers"""
        self.assertEqual(max_integer([-10, -45, -34, -20]), -10)

    def test_mixed_ints(self):
        """Testing with a list of both positive and negative
            integers
        """
        self.assertEqual(max_integer([-10, -39, 8, 5, 34]), 34)

    def test_floats(self):
        """Testing the function with floats"""
        self.assertEqual(max_integer([19.2, 23.5, 34.4]), 34.4)

    def test_large_ints(self):
        """Testing the function with large positive integers"""
        self.assertEqual(max_integer([100000, 190000, 15000]), 190000)

    def test_large_negative_ints(self):
        """Testing the function with large negative integers"""
        self.assertEqual(max_integer([-123000, -110000, 90000]), 90000)

    def test_mixed_positive_negative_ints(self):
        """Testing the function with large signed integers."""
        self.assertEqual(max_integer([-120000, 100000, -1000000]), 100000)


if __name__ == "__main__":
    unittest.main()
