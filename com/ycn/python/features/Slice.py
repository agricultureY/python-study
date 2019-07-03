#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  切片  ###########

# list切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取1-4
print(L[1:4])
# 取最后两个
print(L[-2:])

L_num = list(range(100))
# 前10个数，每两个取一个
print(L_num[:10:2])
# 所有数，每5个取一个
print(L_num[::5])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)[::2])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[::2])
