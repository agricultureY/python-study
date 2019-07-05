#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  map() and reduce()  ###########
from functools import reduce


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下
def f(x):
    return x * x


# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 一个序列求和，就可以用reduce实现
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))
print(sum([1, 3, 5, 7, 9]))


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]), '<--->', type(reduce(fn, [1, 3, 5, 7, 9])))


# 把str转换为int
def char2num(s):
    digist = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digist[s]


print(reduce(fn, map(char2num, '13579')), '<--->', type(reduce(fn, map(char2num, '13579'))))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn_int(x, y):
        return x * 10 + y

    def char2num_int(sc):
        return DIGITS[sc]

    return reduce(fn_int, map(char2num_int, s))


print(str2int('13579'), '<--str2int-->', type(str2int('13579')))


# lambda函数进一步简化
def char2num_lambda(s):
    return DIGITS[s]


def str2int_lambda(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num_lambda, s))


print(str2int_lambda('13579'), '<--str2int_lambda-->', type(str2int_lambda('13579')))
print('<==================================================>')


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name[:1].upper() + name[1:].lower()


print(list(map(normalize, ['adam', 'LISA', 'barT'])))


# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda m, n: m * n, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
CHAR_TO_FLOAT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
