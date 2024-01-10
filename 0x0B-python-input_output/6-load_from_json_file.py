#!/usr/bin/python3
"""
A Function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    filename: the JSON file.
    """
    with open(filename, 'r') as myfile:
        for line in myfile:
            myobj = json.load(line)
    return myobj
