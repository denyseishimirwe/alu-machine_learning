#!/usr/bin/env python3
"""Pooling on images."""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Perform pooling on images.

    Args:
        images: numpy.ndarray of shape (m, h, w, c)
        kernel_shape: tuple (kh, kw)
        stride: tuple (sh, sw)
        mode: 'max' or 'avg'

    Returns:
        numpy.ndarray containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    pool_h = ((h - kh) // sh) + 1
    pool_w = ((w - kw) // sw) + 1
    pooled = np.zeros((m, pool_h, pool_w, c))

    for i in range(pool_h):
        for j in range(pool_w):
            window = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            if mode == 'max':
                pooled[:, i, j, :] = np.max(window, axis=(1, 2))
            else:
                pooled[:, i, j, :] = np.mean(window, axis=(1, 2))

    return pooled
