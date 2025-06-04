#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Convert a Python object into a JSON-formatted string

    Args:
        my_obj (any): the object to convert

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
