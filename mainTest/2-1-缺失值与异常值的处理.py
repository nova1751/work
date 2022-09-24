#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# 对缺失值的处理
df = pd.read_csv('bike-sharing-demand_2/train.csv', encoding='gbk')

print(df.duplicated().value_counts())
# 发现并没有重复的值

# 查找是否有缺失的值
# print(df.isnull())
# print(df.isnull().any())
print(df[df.isnull().values==True])
# 发现并没有缺失的值

# 对异常值的处理
print(df.describe())
# 发现并没有明显异常

# 删除无用的列 datetime casual register 便与后续数据处理
df = df.drop(['datetime','casual','registered'],axis=1)
df.to_csv('train0.csv')


