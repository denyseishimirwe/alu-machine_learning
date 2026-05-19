#!/usr/bin/env python3
"""Module that calculates the minor matrix of a matrix."""


determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Return the minor matrix of a non-empty square matrix.

    Args:
        matrix: a list of lists representing the matrix.

    Returns:
        A new list of lists where entry [i][j] is the determinant of
        the submatrix obtained by removing row i and column j.

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

    if n == 1:
        return [[1]]

    result = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [[matrix[a][b] for b in range(n) if b != j]
                   for a in range(n) if a != i]
            row.append(determinant(sub))
        result.append(row)
    return result
