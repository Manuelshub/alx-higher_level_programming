#!/usr/bin/python3
"""
Function that returns True of False if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is an isntance of the class a_class,
    Otherwise False
    """
    return type(obj) == a_class
