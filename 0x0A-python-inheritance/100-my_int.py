#!/usr/bin/python3
""" A class MyInt that inherits from an int.
"""


class MyInt(int):
    """ Inherits from an integer.
    """
    def __new__(cls, value):
        """
        Initializes the class
        """
        return super(MyInt, cls).__new__(cls, value)

    def __eq__(self, other):
        """ Overrides equality to behave like inequality
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Overrides inequality to behave like equality
        """
        return super().__eq__(other)
