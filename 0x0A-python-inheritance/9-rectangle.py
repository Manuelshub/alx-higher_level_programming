#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Implemeting the area method, that just raises an Exception before
        by returning the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
