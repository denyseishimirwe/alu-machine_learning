#!/usr/bin/env python3
"""Module that concatenates two 2D matrices along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis.

    Args:
        mat1: a 2D matrix of ints/floats.
        mat2: a 2D matrix of ints/floats.
        axis: the axis along which to concatenate (0 or 1).

    Returns:
        A new 2D matrix, or None if the two matrices cannot be
        concatenated along the given axis.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    return None