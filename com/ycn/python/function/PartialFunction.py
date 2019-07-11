#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  偏函数  ###########
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点

import functools

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('12345', base=8))
print(int('12345', base=16))
# functools.partial就是帮助我们创建一个偏函数的，作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单