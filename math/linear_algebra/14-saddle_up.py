#!/usr/bin/env python3
"""Module that performs matrix multiplication with numpy."""
import numpy as np


def np_matmul(mat1, mat2):
    """Perform matrix multiplication.

    Args:
        mat1: a numpy.ndarray.
        mat2: a numpy.ndarray.

    Returns:
        A new numpy.ndarray that is the product mat1 x mat2.
    """
    return np.matmul(mat1, mat2)