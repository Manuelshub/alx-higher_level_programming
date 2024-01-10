#!/usr/bin/python3
import json
"""
A Function that returns the JSON representation of an object.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    my_obj: the object to be represented.
    """
    my_json = json.dumps(my_obj)
    return my_json
