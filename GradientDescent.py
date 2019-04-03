#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
#This is a sample to simulate a function y = theta1*x1 + theta2*x2
input_x = [[1,4], [2,5], [5,1], [4,2]]
y = [19, 26,19,20]
theta = [1,1]
loss = 10
step_size = 0.001
eps = 0.0001
max_iters = 10000
error = 0
iter_count = 0
while( loss > eps and iter_count < max_iters):
    loss = 0
    # 这里更新权重的时候所有的样本点都用上了
    for i in range(3):
        pred_y = theta[0] * input_x[i][0] + theta[1] * input_x[i][1]
        theta[0] = theta[0] - step_size * (pred_y - y[i]) * input_x[i][0]
        theta[1] = theta[1] - step_size * (pred_y - y[i]) * input_x[i][1]

    # 每一次选取随机的一个点进行权重的更新
    # i = random.randint(0, 3)
    # pred_y = theta[0] * input_x[i][0] + theta[1] * input_x[i][1]
    # theta[0] = theta[0] - step_size * (pred_y - y[i]) * input_x[i][0]
    # theta[1] = theta[1] - step_size * (pred_y - y[i]) * input_x[i][1]

    # 注意这里，我这里批量每次选取的是2个样本点做更新，另一个点是随机点+1的相邻点
    # i = random.randint(0, 3)
    # j = (i + 1) % 4
    # pred_y = theta[0] * input_x[i][0] + theta[1] * input_x[i][1]
    # theta[0] = theta[0] - step_size * (pred_y - y[i]) * input_x[i][0]
    # theta[1] = theta[1] - step_size * (pred_y - y[i]) * input_x[i][1]
    #
    # pred_y = theta[0] * input_x[j][0] + theta[1] * input_x[j][1]
    # theta[0] = theta[0] - step_size * (pred_y - y[j]) * input_x[j][0]
    # theta[1] = theta[1] - step_size * (pred_y - y[j]) * input_x[j][1]

    for i in range(3):
        pred_y = theta[0] * input_x[i][0] + theta[1] * input_x[i][1]
        error = 0.5 * (pred_y - y[i]) ** 2
        loss = loss + error
    iter_count += 1
    print 'iters_count', iter_count


print 'theta\t:',theta
print 'final loss\t:',loss
print 'iters\t:',iter_count

print