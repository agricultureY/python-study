#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  python常用内置函数  http://docs.python.org/3/library/functions.html#abs  ###########
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

# abs取模
print(abs(10))
print(abs(-10))
# max()、min()取最大、最小
ll = [1, 2, 3, 4, -5, -7]
print(max(ll))
print(min(ll))
# 数据类型转换
print(type(int('123')))
print(type(float('12.34')))
print(type(str(123)))
print(type(bool('')))
# hex转换16进制
print(hex(11))
