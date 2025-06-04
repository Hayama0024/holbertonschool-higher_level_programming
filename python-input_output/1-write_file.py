#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8), create/overwrite it if needed

    Args:
        filename (str): the name of the file
        text (str): the text to write

    Returns:
        int: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
