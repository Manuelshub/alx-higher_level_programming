#!/usr/bin/python3
"""
Function that returns True if the object is an instance of the class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the class,
    Or an instance of a class that inherited from the class
    """
    if isinstance(obj, a_class):
        return True
    return False
