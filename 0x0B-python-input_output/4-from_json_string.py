#!/usr/bin/python3
import json
"""
A Function that returns an object represented by a JSON string.
"""


def from_json_string(my_str):
    """
    Returns an object representation of a JSON string
    my_str: the JSON string
    """
    my_obj = json.loads(my_str)
    return (my_obj)
