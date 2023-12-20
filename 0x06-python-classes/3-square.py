#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """
    This square class has an instance attribute size.
    This size is set during instantiation with an optional value of 0.
    """
    def __init__(self, size=0):
        """
        This is the constructor method for square class.
        It checks if the size is an integer and if it's not less than 0.
        If these conditions are not met, it raises an exception.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    This is a public method that returns the current square area.
    """
    def area(self):
        return self.__size * self.__size
