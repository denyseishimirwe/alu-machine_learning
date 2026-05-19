#!/usr/bin/env python3
"""Module that adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Add two 2D matrices element-wise.

    Args:
        mat1: a 2D matrix of ints/floats.
        mat2: a 2D matrix of ints/floats.

    Returns:
        A new 2D matrix with the element-wise sums, or None if mat1
        and mat2 do not have the same shape.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
