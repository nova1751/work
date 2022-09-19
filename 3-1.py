#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def returnIndex(arr):
    colIndex = []
    m = arr.shape[0]
    for i in range(m):
        if arr[i][0] > 0 and arr[i][1] < 0:
            colIndex.append(i)
    return colIndex


arr1 = np.random.randn(200, 2)
print(returnIndex(arr1))
