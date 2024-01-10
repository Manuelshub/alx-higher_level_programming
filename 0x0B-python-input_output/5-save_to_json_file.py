#!/usr/bin/python3
import json
"""
A function that writes an object to a text file using a JSON repesentation
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file.
    my_obj: the object to be written.
    filename: the text file
    """
    my_str = json.dumps(my_obj)
    with open(filename, 'w') as myfile:
        myfile.write(my_str)
