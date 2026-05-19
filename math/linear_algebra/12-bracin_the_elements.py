#!/usr/bin/env python3
"""Module that performs element-wise numpy operations."""


def np_elementwise(mat1, mat2):
    """Perform element-wise add, subtract, multiply, and divide.

    Args:
        mat1: an array-like interpretable as a numpy.ndarray.
        mat2: an array-like interpretable as a numpy.ndarray.

    Returns:
        A tuple containing the element-wise sum, difference,
        product, and quotient, respectively.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
