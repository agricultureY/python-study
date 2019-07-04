#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  迭代  ###########
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。在Python中，迭代是通过for ... in来完成的
from collections.abc import Iterable
from collections.abc import Iterator

for ch in 'ABC':
    print(ch)

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, val in enumerate(['a', 'b', 'c']):
    print(i, '<-------->', val)

#   ##########  迭代器  ###########
# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 通过collections模块的Iterable类型判断一个对象是否为可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print('<==============================================>')

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 通过collections模块的Iterator类型判断一个对象是否为迭代(Iterator)对象
print(isinstance('abc', Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((x for x in range(10)), Iterator))
print('<==============================================>')

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的
#   #######  小结  ########
# 凡是可作用于for循环的对象都是Iterable类型；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
# Python的for循环本质上就是通过不断调用next()函数实现的
