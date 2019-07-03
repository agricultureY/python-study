#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  定义函数  ###########
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple

# 引入math库
import math


# 自定义abs函数
def my_abs(x):
    # 参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-23))


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解
def quadratic(a, b, c):
    return ((-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)), ((-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a))


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
