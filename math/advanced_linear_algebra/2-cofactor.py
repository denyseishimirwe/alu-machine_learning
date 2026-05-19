#!/usr/bin/env python3
"""Module that calculates the cofactor matrix of a matrix."""


minor = __import__('1-minor').minor


def cofactor(matrix):
    """Return the cofactor matrix of a non-empty square matrix.

    Args:
        matrix: a list of lists representing the matrix.

    Returns:
        A new list of lists where entry [i][j] is (-1)^(i+j) times
        the (i, j) minor of matrix.

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

    m = minor(matrix)
    return [[((-1) ** (i + j)) * m[i][j] for j in range(n)]
            for i in range(n)]
