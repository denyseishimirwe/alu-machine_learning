#!/usr/bin/env python3
"""Convolution on grayscale images with custom padding."""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Perform a convolution on grayscale images with custom padding.

    Args:
        images: numpy.ndarray of shape (m, h, w)
        kernel: numpy.ndarray of shape (kh, kw)
        padding: tuple of (ph, pw)

    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    padded = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw)),
        mode='constant',
        constant_values=0,
    )
    conv_h = h + (2 * ph) - kh + 1
    conv_w = w + (2 * pw) - kw + 1
    convolved = np.zeros((m, conv_h, conv_w))

    for i in range(conv_h):
        for j in range(conv_w):
            convolved[:, i, j] = (
                padded[:, i:i + kh, j:j + kw] * kernel
            ).sum(axis=(1, 2))

    return convolved
