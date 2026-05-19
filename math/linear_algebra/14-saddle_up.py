#!/usr/bin/env python3
"""Module that performs matrix multiplication using numpy."""
import numpy as np


def np_matmul(mat1, mat2):
    """Return the matrix product of mat1 and mat2.

    Args:
        mat1: a numpy.ndarray.
        mat2: a numpy.ndarray.

    Returns:
        A new numpy.ndarray equal to mat1 @ mat2.
    """
    return np.matmul(mat1, mat2)
