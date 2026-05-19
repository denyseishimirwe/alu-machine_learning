#!/usr/bin/env python3
"""Module that performs matrix multiplication."""


def mat_mul(mat1, mat2):
    """Perform matrix multiplication.

    Args:
        mat1: a 2D matrix of ints/floats.
        mat2: a 2D matrix of ints/floats.

    Returns:
        A new 2D matrix that is the product mat1 x mat2, or None if
        the two matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for row in mat1:
        new_row = []
        for j in range(len(mat2[0])):
            total = 0
            for k in range(len(mat2)):
                total += row[k] * mat2[k][j]
            new_row.append(total)
        result.append(new_row)
    return result