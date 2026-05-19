#!/usr/bin/env python3
"""Module that concatenates two numpy.ndarrays along an axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis.

    Args:
        mat1: an array-like interpretable as a numpy.ndarray.
        mat2: an array-like interpretable as a numpy.ndarray.
        axis: the axis along which to concatenate.

    Returns:
        A new numpy.ndarray with mat1 and mat2 concatenated.
    """
    return np.concatenate((mat1, mat2), axis=axis)
