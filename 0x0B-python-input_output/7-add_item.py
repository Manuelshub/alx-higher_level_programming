#!/usr/bin/python3
import sys
import json
"""
A Script that adds all arguments to a python list and save them to a file
"""


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    args = load_from_json_file(filename)
    if args == FileNotFoundError:
        args = []
    args.extend(sys.argv[1:])
    save_to_json_file(args, filename)
