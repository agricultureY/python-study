#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  列表生成器  ###########
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# 列表生成式生成1-10的平方
print([x * x for x in range(1, 11)])
# 列表生成式生成1-10仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])
# 使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列表生成式使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
