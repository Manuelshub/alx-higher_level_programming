#!/usr/bin/python3
"""
A class Student
"""


class Student:
    """ Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """ Method that initializes the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This method retriees a dictionary representation of a
        class instance.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """ This method replaces all attributes of a class instance
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
