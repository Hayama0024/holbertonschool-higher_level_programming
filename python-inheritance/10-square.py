#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a square with size, ensuring it's a positive integer."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Rectangle] {self.__size}/{self.__size}"
