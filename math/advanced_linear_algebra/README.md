# Advanced Linear Algebra

This project covers determinants, minors, cofactors, the adjugate
matrix, matrix inverses, and the definiteness of a matrix.

## Requirements

- Ubuntu 16.04 LTS
- Python 3.5
- numpy 1.15
- pycodestyle 2.5

All scripts start with `#!/usr/bin/env python3`, are executable, end
with a newline, and follow `pycodestyle`. Modules, classes, and
functions are documented.

## Files

| File | Description |
| --- | --- |
| `0-determinant.py` | `determinant(matrix)` — determinant via cofactor expansion. |
| `1-minor.py` | `minor(matrix)` — minor matrix. |
| `2-cofactor.py` | `cofactor(matrix)` — cofactor matrix. |
| `3-adjugate.py` | `adjugate(matrix)` — adjugate (transpose of cofactors). |
| `4-inverse.py` | `inverse(matrix)` — inverse, or `None` if singular. |
| `5-definiteness.py` | `definiteness(matrix)` — classifies a symmetric `numpy.ndarray`. |
