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

    @property
    def size(self):
        """
        The size getter
        Returns the value of the attribute size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This is the size setter
        It sets the value of size with value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """
        This method assignes attributes
        Args:
            (*args): the list of arguments(no keyworded arguments)
            (**kwargs): keyworded arguments
        If *args exists skip **kwargs.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This returns the dictionary representation of
            the class square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
