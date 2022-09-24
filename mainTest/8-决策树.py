#!/user/bin/env python3
# -*- coding: utf-8 -*-
print(__doc__)
import operator

# 计算基尼指数
def calcGini(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    gini = 0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        gini += prob * (1 - prob)
    return gini

# 划分数据集
def splitDataSet(dataSet, index, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[index] == value:
            reducedFeatVec = featVec[:index]
            retDataSet.append(reducedFeatVec)
    return retDataSet

# 选择最好的数据集，每个都选择
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcGini(dataSet)
    bestFeature = -1
    bestGini, newGini = 100, 0.0
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newGini += prob * calcGini(subDataSet)
        if (newGini < bestGini):
            bestGini = newGini
            bestFeature = i
    return bestFeature


# 多数表决
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# 采用递归的方法创建树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

