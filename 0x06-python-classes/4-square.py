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
        self.size = size

    @property
    def size(self):
        """
        This is the size getter.
        It returns the value of the private instance attribute __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the size setter.
        It checks if the value is an integer and if it's not less than 0.
        If these conditions are not met, it raises an exception.
        Otherwise, it sets the value of the private instance attribute __size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method calculates and returns the area of the square.
        """
        return self.__size * self.__size
