#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a specified class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or its subclass."""
    return isinstance(obj, a_class)
