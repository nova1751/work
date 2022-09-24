#!/user/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import pandas as pd
import matplotlib.pylab as plt

# 加载数据集
def loadDataSet(filename):
    df = pd.read_csv(filename)
    mainMat = df.values
    m, n = mainMat.shape
    dataMat = []
    labelMat = []
    dataMat = mainMat[:, 0:m - 1]
    labelMat = mainMat[:, -1]
    return dataMat, labelMat

# 最小二乘法
def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

# 画图测试
def regression1():
    xArr, yArr = loadDataSet("train0.csv")
    xMat = mat(xArr)
    ws = standRegres(xArr, yArr)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    ax.plot(xCopy[:, 1], yHat)
    plt.show()

# 岭回归
def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam
    if linalg.det(denom) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = denom.I * (xMat.T * yMat)
    return ws

# 测试
def ridgeTest(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i - 10))
        wMat[i, :] = ws.T
    return wMat


def regression3():
    abX, abY = loadDataSet("train0.csv")
    ridgeWeights = ridgeTest(abX, abY)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()


if __name__ == '__main__':
    # regression1()  # 普通线性回归
    regression3()    # 正则化后的岭回归
