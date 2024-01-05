#!/usr/bin/python3
"""
A class that defines a Rectangle.
"""


class Rectangle:

    """ A public class attribute, initialized to 0"""
    number_of_instances = 0

    """ A public attribute, initialized with '#'"""
    print_symbol = "#"

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

        """ Incremented during each new instance instantiation"""
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
        rec = []
        for i in range(self.height):
            [rec.append(str(self.print_symbol)) for j in range(self.width)]
            if i != self.height - 1:
                rec.append("\n")
        return ("".join(rec))

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

        """ Decremented during each instance deletion"""
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compare the areas of two rectangles and return the bigger or equal one
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
