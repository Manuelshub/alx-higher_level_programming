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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        This public method returns the area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        This method prints to stdout the Retangle instance with the
        character '#'
        """
        if self.height == 0 or self.width == 0:
            print("")
            return
        for c in range(self.height):
            for b in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        This prints the string representation of the class
        """
        clss_name = self.__class__.__name__
        Id = self.id
        height = self.height
        width = self.width
        return f"[{clss_name}] ({Id}) {self.x}/{self.y} - {width}/{height}"
