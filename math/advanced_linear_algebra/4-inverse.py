#!/usr/bin/env python3
"""Module that calculates the inverse of a matrix."""


determinant = __import__('0-determinant').determinant
adjugate = __import__('3-adjugate').adjugate


def inverse(matrix):
    """Return the inverse of a non-empty square matrix.

    Args:
        matrix: a list of lists representing the matrix.

    Returns:
        A new list of lists equal to the inverse of matrix, or
        ``None`` if matrix is singular.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is empty or not square.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if matrix == [[]] or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]
