#!/usr/bin/python3
""" Function that returns teh dictionary description with simple data
structure.
"""


def class_to_json(obj):
    """ Returns a dictionary description with simple data structure
    """
    if isinstance(obj, (int, str, bool, type(None))):
        return obj
    elif isinstance(obj, list):
        obj_list = []
        for item in obj:
            obj_list.append(class_to_json(item))
        return obj_list
    elif isinstance(obj, dict):
        result_dict = {}
        for key, value in obj.items():
            result_dict[key] = class_to_json(value)
        return result_dict
    elif hasattr(obj, '__dict__'):
        return class_to_json(obj.__dict__)
    else:
        result_dict = {
            '__class__': obj.__class__.__name__,
            '__module__': obj.__module__,
            'attributes': {}
        }

        for key in dir(obj):
            if not key.startswith('_') and key not in ['__str__']:
                result_dict['attributes'][key] =\
                    class_to_json(getattr(obj, key))
        return result_dict
