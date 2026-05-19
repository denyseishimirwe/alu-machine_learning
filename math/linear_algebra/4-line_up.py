#!/usr/bin/env python3
"""Module that adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Add two arrays element-wise.

    Args:
        arr1: a list of ints/floats.
        arr2: a list of ints/floats.

    Returns:
        A new list with the element-wise sums, or None if arr1 and
        arr2 do not have the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]