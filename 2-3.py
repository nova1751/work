#!/user/bin/env python3
# -*- coding: utf-8 -*-

def bestProfit(arr):
    income = 0
    n = len(arr)
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            income += arr[i + 1] - arr[i]
        else:
            income += 0
    return income
arr1, arr2, arr3 = [7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]
print(bestProfit(arr1), bestProfit(arr2), bestProfit(arr3))
