#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def sorted(gradesList, m, N):  # 排序函数
    list0 = np.array([])
    for i in range(m):
        list0 = np.append(list0, sum(gradesList[i]))
    indicies = list0.argsort()[::-1]
    return indicies # 返回索引


def search(gradesList, N, m):  # 搜索函数
    indices = []
    for i in range(N):
        for j in range(m):
            if gradesList[i][j] < 60:
                indices.append(i)
            break
    return indices


def print0(indicies, idlist, N):  # 打印函数
    for i in range(int(N / 5) + 1):
        print(idlist[indicies[i]])


if __name__ == '__main__':
    N, m = list(map(int, input().split()))
    idList = []
    nameList = []
    sexList = []
    gradesList = []
    for i in range(N):
        idList.append(input())
        nameList.append(input())
        sexList.append(input())
        gradesList.append(list(map(int, input().split())))

    index = sorted(gradesList, m, N)
    print0(index, idList, N)
    for i in search(gradesList,N,m):
        print(nameList[i])