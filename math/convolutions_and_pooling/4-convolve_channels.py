#!/usr/bin/env python3
"""Convolution on images with channels."""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """Perform a convolution on images with channels.

    Args:
        images: numpy.ndarray of shape (m, h, w, c)
        kernel: numpy.ndarray of shape (kh, kw, c)
        padding: tuple (ph, pw), 'same', or 'valid'
        stride: tuple (sh, sw)

    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(((h - 1) * sh + kh - h) / 2)
        pw = int(((w - 1) * sw + kw - w) / 2)
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant',
        constant_values=0,
    )
    conv_h = ((h + 2 * ph - kh) // sh) + 1
    conv_w = ((w + 2 * pw - kw) // sw) + 1
    convolved = np.zeros((m, conv_h, conv_w))

    for i in range(conv_h):
        for j in range(conv_w):
            convolved[:, i, j] = (
                padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :] * kernel
            ).sum(axis=(1, 2, 3))

    return convolved
