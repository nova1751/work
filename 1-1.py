#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 一维高斯分布的随机KL散度的计算公式为:
# KL(p,q) = log(o2/o1) + (o1^2+(u1-u2)^2)/2*o2^2-1/2

from math import log

u1, u2 = 5, -5
o1, o2 = 1, 1
KL = float(log(o2 / o1, 2) + (o1 ** 2 + (u1 - u2) ** 2) / 2 * o2 ** 2 - 1 / 2)
print('KL散度为：', KL)
# KL散度为： 50.0

