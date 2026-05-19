#!/usr/bin/env python3
"""Module that transposes a numpy.ndarray."""


def np_transpose(matrix):
    """Return the transpose of matrix as a new numpy.ndarray.

    Args:
        matrix: an array-like that can be interpreted as a
            numpy.ndarray.

    Returns:
        A new numpy.ndarray that is the transpose of matrix.
    """
    return matrix.transpose()