#!/usr/bin/python3
"""
A class square that inherits from a class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square by inheriting from a rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the square.
        size(int): the size of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints the string representation of the class
        """
        clss_name = self.__class__.__name__
        width = self.width

        return f"[{clss_name}] ({self.id}) {self.x}/{self.y} - {width}"
