#!/usr/bin/env python3
"""Binomial distribution."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize a binomial distribution.

        Args:
            data: list of data to estimate the distribution
            n: number of Bernoulli trials
            p: probability of a success
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - (variance / mean)
            n = round(mean / p)
            self.n = int(n)
            self.p = float(mean / self.n)

    @staticmethod
    def factorial(n):
        """Calculate factorial of n."""
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def pmf(self, k):
        """Calculate the PMF for a given number of successes.

        Args:
            k: number of successes

        Returns:
            PMF value for k, or 0 if k is out of range
        """
        if type(k) is not int:
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        n_choose_k = (
            self.factorial(self.n) /
            (self.factorial(k) * self.factorial(self.n - k))
        )
        return n_choose_k * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate the CDF for a given number of successes.

        Args:
            k: number of successes

        Returns:
            CDF value for k, or 0 if k is out of range
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
