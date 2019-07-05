#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  函数作为返回值  ###########
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def lazy_sum(*args):
    def _sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return _sum


fn = lazy_sum(1, 2, 3, 4, 5)
print(fn)
print(fn())


# lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count_err():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count_err()
print('f1=', f1(), 'f2=', f2(), 'f3=', f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


ff1, ff2, ff3 = count()
print('ff1=', ff1(), 'ff2=', ff2(), 'ff3=', f3())
