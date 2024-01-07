#!/usr/bin/python3
"""
A fucntion that adds two integers
a: the first number
b: the second number
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    int_a = int(a)
    int_b = int(b)
    return int_a + int_b
