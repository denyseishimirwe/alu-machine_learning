#!/usr/bin/env python3
"""Multivariate Normal distribution."""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize a MultiNormal distribution.

        Args:
            data: numpy.ndarray of shape (d, n) containing the data set
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - self.mean
        self.cov = np.matmul(deviation, deviation.T) / (n - 1)

    def pdf(self, x):
        """Calculate the PDF at a data point.

        Args:
            x: numpy.ndarray of shape (d, 1) containing the data point

        Returns:
            PDF value at x
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        diff = x - self.mean
        cov_inv = np.linalg.inv(self.cov)
        det = np.linalg.det(self.cov)
        exponent = -0.5 * np.matmul(np.matmul(diff.T, cov_inv), diff)
        denom = np.sqrt(((2 * np.pi) ** d) * det)
        return float(np.exp(exponent) / denom)
