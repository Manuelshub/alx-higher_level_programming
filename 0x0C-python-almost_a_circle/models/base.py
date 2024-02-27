#!/usr/bin/python3
""" My class base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns the JSON string representation
            of the list_dictionaries.
        Arg:
            list_dictionaries: a list of dictionary.
        if list_dictionaries is None return the string "[]".
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
