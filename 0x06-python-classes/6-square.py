#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """
    This square class has an instance attribute size.
    This size is set during instantiation with an optional value of 0.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is the constructor method for square class.
        It checks if the size is an integer and if it's not less than 0.
        If these conditions are not met, it raises an exception.
        It also checks if the postion is a tuple of two positive integers.
        If it's not it raises an exception.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This is the size getter.
        It returns the value of the private instance attribute __size.
        """
        return self.__size

    @property
    def position(self):
        """
        This is the position getter.
        It returns the value of the private instance attribute __position.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        This is the position setter.
        It checks if the position is a tuple of two positive integers.
        If it's not it raises an exception.
        """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        This method calculates and returns the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        This method prints in stdout the square with character #
        """
        if self.__size == 0:
            print()
        for h in range(self.__position[1]):
            print()

        for m in range(self.__size):
            for n in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print('#', end='')
            print()
