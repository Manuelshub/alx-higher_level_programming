#!/usr/bin/python3
"""
A function that writes an object to a text file using a JSON repesentation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file.
    my_obj: the object to be written.
    filename: the text file
    """
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
