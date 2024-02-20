#!/usr/bin/python3
import math
"""A class that defines a Circle."""


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius):
        """Initializes an instance of the circle.
        Args:
            radius: the radius of the circle.
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""
        return (2 * math.pi) * self.__radius
