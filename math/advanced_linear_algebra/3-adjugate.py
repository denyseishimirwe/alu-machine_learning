#!/usr/bin/env python3
"""Module that calculates the adjugate matrix of a matrix."""


cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Return the adjugate (transpose of cofactor) of a square matrix.

    Args:
        matrix: a list of lists representing the matrix.

    Returns:
        A new list of lists equal to the transpose of the cofactor
        matrix of matrix.

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

    c = cofactor(matrix)
    return [[c[i][j] for i in range(n)] for j in range(n)]
