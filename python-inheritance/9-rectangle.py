#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that validates width and height, and can compute area."""

    def __init__(self, width, height):
        """
        Initialize a rectangle instance.

        Arguments:
        width -- the width of the rectangle (must be a positive integer)
        height -- the height of the rectangle (must be a positive integer)
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
        The area as an integer.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        A string in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
