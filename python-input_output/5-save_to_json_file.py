#!/usr/bin/python3
"""
Function that writes an object to a text file,
using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a file in JSON format

    Args:
        my_obj (any): the object to serialize
        filename (str): the name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
