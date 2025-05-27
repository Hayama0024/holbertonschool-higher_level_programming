#!/usr/bin/python3
"""
This module defines a class BaseGeometry
with an unimplemented area method.
"""


class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """
        Raises an Exception with a
        message indicating it's not implemented.
        """
        raise Exception("area() is not implemented")
