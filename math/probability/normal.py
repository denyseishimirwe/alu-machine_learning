#!/usr/bin/env python3
"""Normal distribution."""


class Normal:
    """Represents a normal distribution."""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize a normal distribution.

        Args:
            data: list of data to estimate the distribution
            mean: mean of the distribution
            stddev: standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** (1 / 2)

    def z_score(self, x):
        """Calculate the z-score of a given x-value.

        Args:
            x: x-value

        Returns:
            z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score.

        Args:
            z: z-score

        Returns:
            x-value of z
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the PDF for a given x-value.

        Args:
            x: x-value

        Returns:
            PDF value for x
        """
        exponent = (-1 / 2) * (((x - self.mean) / self.stddev) ** 2)
        return (self.e ** exponent) / (self.stddev * ((2 * self.pi) ** (1 / 2)))

    def cdf(self, x):
        """Calculate the CDF for a given x-value.

        Args:
            x: x-value

        Returns:
            CDF value for x
        """
        z = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        erf = (2 / (self.pi ** (1 / 2))) * (
            z - (z ** 3) / 3 + (z ** 5) / 10 - (z ** 7) / 42 + (z ** 9) / 216
        )
        return (1 / 2) * (1 + erf)
