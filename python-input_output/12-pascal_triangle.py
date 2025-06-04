#!/usr/bin/python3
"""
12-pascal_triangle.py
Returns a list of lists representing Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Generate Pascal’s triangle of n rows."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]

        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])

        row.append(1)
        triangle.append(row)

    return triangle
