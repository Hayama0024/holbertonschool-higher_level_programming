#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a square with size, validated and stored privately."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Initialize as a rectangle with equal sides

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
