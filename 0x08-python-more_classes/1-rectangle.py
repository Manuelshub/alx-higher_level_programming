#!/usr/bin/python3
"""
A class that defines a rectangle.
"""


class Rectangle:
    """
    This rectangle class has two attributes width and height.
    Width (int): the width of the rectangle.
    Height (int): the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        This initializes a rectangle.
        Args:
        width: the width of the rectangle.
        height: the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width property of the rectangle.
        Value (int): the width value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Vallue (int): the height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value