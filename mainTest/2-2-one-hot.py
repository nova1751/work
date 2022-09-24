#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# 对缺失值的处理
df = pd.read_csv('titanic/train.csv', encoding='gbk')
# print(df.duplicated().value_counts())
# 发现并没有重复的值

# 查找是否有缺失的值
# print(df.isnull())
# print(df.isnull().any())
# 发现存在缺失的值进行数目不多，进行删除处理
# 先剔除无用的列
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
df.dropna(how='any', axis=0, inplace=True)
dumpies = pd.get_dummies(df['Sex'])
dumpies0 = pd.get_dummies(df['Embarked'])
merged1 = pd.concat([df, dumpies], axis='columns')
merged = pd.concat([merged1, dumpies0], axis='columns')
final = merged.drop(['Sex', 'Embarked'], axis='columns')
print(final[final.isnull().values == True])
final.to_csv('train1.csv')

# 对异常值的处理
print(final.describe())
# 发现并没有明显异常

# 数据处理完毕