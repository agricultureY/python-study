#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  迭代  ###########
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。在Python中，迭代是通过for ... in来完成的
from collections.abc import Iterable

for ch in 'ABC':
    print(ch)

# 通过collections模块的Iterable类型判断一个对象是否为可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, val in enumerate(['a', 'b', 'c']):
    print(i, '<-------->', val)
