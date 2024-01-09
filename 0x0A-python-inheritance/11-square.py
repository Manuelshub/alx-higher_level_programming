#!/usr/bin/python3
"""
A class the defines a square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the square
        size: the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string.
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
