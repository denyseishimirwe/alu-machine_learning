#!/usr/bin/env python3
"""Polynomial derivative."""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial.

    Args:
        poly: list of coefficients; index is the power of x

    Returns:
        New list of derivative coefficients, [0] if derivative is 0,
        or None if poly is invalid
    """
    if type(poly) is not list or len(poly) < 1:
        return None
    if len(poly) == 1:
        return [0]
    return [i * poly[i] for i in range(1, len(poly))]
