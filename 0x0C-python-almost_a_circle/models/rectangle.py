#!/usr/bin/python3
""" A class that defines a Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the rectangle
        width(int): a private instance attribute that gives us the width
        height: a private instance atribute that gives us the height
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        This is the width getter
        It returns the value of the private instance attribute __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is the width setter
        it sets the value of the private instance attribute __width with value
        """
        if value <= 0:
            raise ValueError("value must be greater than 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This is the height getter
        It returns the value of the private instance attribute __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is the height setter
        It sets the value of the private instance attribute __height with value
        """
        if value <= 0:
            raise ValueError("value must be greater than 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        This is x getter
        It returns the value of the private instance attribute __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is x setter
        sets the value of __x with value
        """
        self.__x = value

    @property
    def y(self):
        """
        This is y getter
        It returns the value of __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is y setter
        It sets the value of __y with value
        """
        self.__y = value