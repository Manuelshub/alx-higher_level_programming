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
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string
        """
        return super().__str__()
