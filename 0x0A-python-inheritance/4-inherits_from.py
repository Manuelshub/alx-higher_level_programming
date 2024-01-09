#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returs True if the object is an instance of the class that
    inherited from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
