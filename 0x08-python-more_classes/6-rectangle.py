#!/usr/bin/python3
"""
A class that defines a Rectangle.
"""


class Rectangle:

    number_of_instances = 0

    """
    This Rectangle class has two attributes width and height.
    Width (int): the width of the rectangle.
    Height (int): the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        This initializes the rectangle.
        width: the width of the rectangle.
        height: the height of the rectangle.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width.
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
        Sets the value of the height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return ""
        return "\n".join(['#' * self.width] * self.height)

    def __repr__(self):
        """
        Return a formal string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deletes an instance of the class Rectangle.
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
