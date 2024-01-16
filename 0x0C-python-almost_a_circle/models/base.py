#!/usr/bin/python3
""" My class base
"""


class Base:
    """ This class will be the base of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the class base
        id: (int) the id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
