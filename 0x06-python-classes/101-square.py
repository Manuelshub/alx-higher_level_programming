#!/usr/bin/python3
"""
A class that defines a square.
"""

class Square:
    """
    This class defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiation of the class.
        size: The size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        self.__size = value

    @property
    def position(self):
        """
        This Retrieves the position that is a private instance attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This sets the position(the private instance attribute) to value.
        """
        if type(value) is not tuple and len(value) != 2 and (type(position[0]) is not int and type(position[1])
            is not int):
            raise TypeError('position must be a tuple of 2 positive integer')
        self.__position = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints in stdout the square with character #
        """
        if self.__size == 0:
            print()
        else:
            for h in range(self.__position[1]):
                print()

            for m in range(self.__size):
                for n in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end='')
                print()

    def __str__(self):
        """
        This method prints the strings representation of the class
        """
        square_str = ""
        if self.__size == 0:
            square_str += '\n'
        else:
            for h in range(self.__position[1]):
                square_str += '\n'
            for m in range(self.__size):
                for n in range(self.__position[0]):
                    square_str += " "
                for j in range(self.__size):
                    square_str += '#'
                square_str += '\n'
        return square_str
