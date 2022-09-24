#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 定义偏导的倒数
def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)

# 定义MSE损失函数
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()




