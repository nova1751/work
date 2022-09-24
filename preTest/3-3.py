#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = np.array(pd.read_csv('data.csv'))
n = len(df)
rightDataSet = []
falseDataSet = []
for i in range(n):
    if df[i][3] == df[i][4]:
        rightDataSet.append([df[i][1], df[i][2]])

    else:
        falseDataSet.append([df[i][1], df[i][2]])
print('the rightDataSet is :')
print(np.array(rightDataSet))
print('the falseDataSet is :')
print(np.array(falseDataSet))
