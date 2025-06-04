#!/usr/bin/python3
"""
Function that creates an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON-formatted file

    Args:
        filename (str): the name of the file to read from

    Returns:
        object: the Python data structure represented by the JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
