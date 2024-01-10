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

    def to_json(self):
        """ This method retriees a dictionary representation of a
        class instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
