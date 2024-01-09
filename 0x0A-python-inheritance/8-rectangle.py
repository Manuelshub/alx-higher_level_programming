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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
A class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    A class that defines a rectangle
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle
        width: the width of the rectangle
        height: the height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
