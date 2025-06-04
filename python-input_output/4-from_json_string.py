#!/usr/bin/python3
"""
Function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string into a Python object

    Args:
        my_str (str): JSON-formatted string

    Returns:
        object: the corresponding Python data structure
    """
    return json.loads(my_str)
