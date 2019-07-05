#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  filter()  ###########
# filter()函数用于过滤序列，接收一个函数和一个序列，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
# 在一个list中，删掉偶数，只保留奇数
def is_odd(m):
    return m % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 求素数
# 定义无限序列生成器
def _odd_iter():
    n = 2
    while True:
        n = n + 1
        yield n


# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始化序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for q in primes():
    if q < 100:
        print(q)
    else:
        break
