#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The inputs can be integers or floats.
Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers (int or float) after casting to integers.

    Args:
        a: First number
        b: Second number (default is 98)

    Returns:
        The integer result of a + b

    Raises:
        TypeError: If either a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
