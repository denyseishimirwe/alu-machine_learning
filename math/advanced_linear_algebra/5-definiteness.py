#!/usr/bin/env python3
"""Module that determines the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """Return a string describing the definiteness of matrix.

    Args:
        matrix: a numpy.ndarray of shape (n, n).

    Returns:
        One of ``"Positive definite"``, ``"Positive semi-definite"``,
        ``"Negative semi-definite"``, ``"Negative definite"``, or
        ``"Indefinite"``. Returns ``None`` if matrix is not a valid
        (square, symmetric, non-empty) matrix or does not fit any of
        the categories above.

    Raises:
        TypeError: if matrix is not a numpy.ndarray.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if (matrix.ndim != 2 or matrix.shape[0] == 0 or
            matrix.shape[0] != matrix.shape[1]):
        return None

    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues, _ = np.linalg.eig(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    if np.all(eigenvalues < 0):
        return "Negative definite"
    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    if np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"
    return None
