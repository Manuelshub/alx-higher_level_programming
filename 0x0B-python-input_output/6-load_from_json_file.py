#!/usr/bin/python3
import json
"""
A Function that creates an Object from a JSON file
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    filename: the JSON file.
    """
    with open(filename, 'r') as myfile:
        for line in myfile:
            myobj = json.loads(line)
    return myobj
