#!/usr/bin/env python3
"""Polynomial integral."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial.

    Args:
        poly: list of coefficients; index is the power of x
        C: integration constant (integer)

    Returns:
        New list of integral coefficients (as small as possible),
        or None if poly or C is invalid
    """
    if type(poly) is not list or len(poly) == 0 or type(C) is not int:
        return None
    for coeff in poly:
        if type(coeff) not in (int, float):
            return None

    integral = [C]
    for power, coeff in enumerate(poly):
        val = coeff / (power + 1)
        if val == int(val):
            val = int(val)
        integral.append(val)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
