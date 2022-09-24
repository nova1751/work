#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy
from numpy import *


def matDot(mat1, mat2): # 基础循环做法
    m, n = mat1.shape
    n, t = mat2.shape
    returnMat = zeros((m, t))
    for i in range(m):
        for p in range(t):
            x = 0
            for j in range(n):
                line = []
                x += mat1[i][j] * mat2[j][p]
            returnMat[i][p] = x
    return returnMat

def matDot0(mat1, mat2): # 调用函数对矩阵乘法进行优化
    m, n = mat1.shape
    n, t = mat2.shape
    returnMat = zeros((m,t))
    for i in range(m):
        for p in range(t):
            x = 0
            x=sum(mat1[i,:]*mat2[:,p])
            returnMat[i][p] = x
    return returnMat

mat1 = numpy.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
mat2 = numpy.array([[1, 1],
                   [2, 2],
                   [1, 1]])
# print(sum(mat2[:,0]*mat1[0,:]))
print(matDot0(mat1, mat2))
