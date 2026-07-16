#!/usr/bin/env python3
"""Summation of i squared from 1 to n."""


def summation_i_squared(n):
    """Calculate the sum of squares from 1 to n.

    Args:
        n: stopping condition (positive integer)

    Returns:
        Integer sum, or None if n is invalid
    """
    if type(n) is not int or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
