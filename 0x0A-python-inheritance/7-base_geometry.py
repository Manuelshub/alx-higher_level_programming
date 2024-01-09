#!/usr/bin/python3
"""
A class Base Geometry
"""


class BaseGeometry:
    """
    Defines a class BaseGeometry
    """
    def area(self):
        """
        This method just raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates a value
        value: the value to be validated
        name: the name associated with the value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
