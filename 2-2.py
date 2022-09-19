#!/user/bin/env python3
# -*- coding: utf-8 -*-

def jump(array):
    i, res = 0, 0
    arrLen = len(array)
    while (i < arrLen - 1):
        steps = array[i]
        if steps >= arrLen - 1 - i:
            res += 1
            break
        max = array[i + 1]
        index = i + 1
        j = index
        while (j <= i + steps and j < arrLen - 1):
            if (array[j] + j - index >= max):
                max = array[j]
                index = j
            j += 1
        res += 1
        i = index
    return res

arr1,arr2 = [2,3,1,1,4],[2,3,0,1,4]
print(jump(arr1),jump(arr2))

