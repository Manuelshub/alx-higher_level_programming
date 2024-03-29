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

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON rep of a list_objs to a file."""
        subcls_name = cls.__name__
        filename = f"{subcls_name}.json"

        if list_objs is None:
            json_string = "[]"
        else:
            list_dicts = [dct.to_dictionary() for dct in list_objs]
            json_string = cls.to_json_string(list_dicts)

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """This methods returns the list of JSON representation
            Args:
                json_string: a string representing a list 0f dictionaries
            If json_string is None, return an empty list
            Otherwise return the list represented by json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method returns an instance with all attributes already set
            Args:
                dictionary: a double pointer to a dictionary
        """
        if cls.__name__ == 'Rectangle':
            update_inst = cls(1, 1)
        elif cls.__name__ == 'Square':
            update_inst = cls(1)
        update_inst.update(**dictionary)
        return update_inst
