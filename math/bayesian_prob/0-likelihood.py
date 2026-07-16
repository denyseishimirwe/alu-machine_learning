#!/usr/bin/env python3
"""Binomial likelihood."""

import math
import numpy as np


def likelihood(x, n, P):
    """Calculate the likelihood of obtaining the data given probabilities.

    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray of hypothetical probabilities

    Returns:
        1D numpy.ndarray of likelihoods for each probability in P
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    binomial_coeff = math.factorial(n) / (
        math.factorial(x) * math.factorial(n - x)
    )
    return binomial_coeff * (P ** x) * ((1 - P) ** (n - x))
