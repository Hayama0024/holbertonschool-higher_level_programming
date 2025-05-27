#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height (validated)."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
