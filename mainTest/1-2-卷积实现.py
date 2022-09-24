#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def convolve(mat, filter):
    m, n = mat.shape
    if max(m, n) <= 3:
        return str('Matrix shape error!!!')
    returnMat = np.zeros((m - 3 + 1, n - 3 + 1))
    for i in range(n - 3 + 1):
        for j in range(m - 3 + 1):
            x = 0
            x = np.vdot(mat[i:i + 3, j:j + 3], filter)
            returnMat[i][j] = x
    return returnMat


mat = np.array([[1, 1, 1, 1],
                [1, 3, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]])
filter = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
print(convolve(mat, filter))
