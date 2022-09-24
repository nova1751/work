#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 矩阵的无穷范数为矩阵行元素绝对值之和的最大值
import numpy as np

arr = np.array([[999, 1, 0.1],
                [321, -666, 12],
                [-418, 203, 358]])
infiNorm = max(np.sum(np.abs(arr), axis=1))
print('无穷范数为：', infiNorm)
# 无穷范数为： 1000.1