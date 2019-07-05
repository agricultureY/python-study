#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  sorted()  ###########
# 排序算法
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来
L_num = [36, 5, -12, 9, -21]
L_str = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L_num))
# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
# 例如按绝对值大小排序
print(sorted(L_num, key=abs))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted(L_str))
# 忽略大小写排序
print(sorted(L_str, key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(L_num, key=None, reverse=True))
