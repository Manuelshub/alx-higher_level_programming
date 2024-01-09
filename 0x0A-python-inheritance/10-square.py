#!/usr/bin/python3
"""
Defines a square that inherits from a class Rectagle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines the class Square that inherits from the class Rectangle
    that inherits from Basegeometry
    """
    def __init__(self, size):
        """
        Initializes the class Square
        size(int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
