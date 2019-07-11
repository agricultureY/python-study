#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  装饰器  ###########
import datetime
import functools
import time


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
# 函数对象有一个__name__属性，可以拿到函数的名字
# 现在，假设我们要增强nowTime()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
def log(fun):
    def wrapper(*args, **kw):
        print('call %s():' % fun.__name__)
        return fun(*args, **kw)

    return wrapper


# 观察log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
# 把@log放到nowTime()函数的定义处，相当于执行了语句:nowTime=log(nowTime)
# 由于log()是一个decorator，返回一个函数，所以，原来的nowTime()函数仍然存在，只是现在同名的nowTime变量指向了新的函数，于是调用nowTime()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def modelLog(text):
    def decorator(fun):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, fun.__name__))
            return fun(*args, **kw)

        return wrapper

    return decorator


# 把@modelLog放到nowTime()函数的定义处，相当于执行了语句:nowTime=log('execute')(nowTime
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是nowTime函数，返回值最终是wrapper函数)
# 过decorator装饰之后的函数，它们的__name__已经从原来的'nowTime'变成了'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中
# Python内置的functools.wraps可以把原始函数的__name__等属性复制到wrapper()函数中
def fullLog(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print('call %s():' % fun.__name__)
        return fun(*args, **kw)

    return wrapper


def fullModelLog(text):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, fun.__name__))
            return fun(*args, **kw)

        return wrapper

    return decorator


# @log
# @modelLog('execute')
# @fullLog
@fullModelLog('execute')
def nowTime():
    print(datetime.datetime.now())


_time = nowTime
print(nowTime.__name__, '<---->', time.__name__)
nowTime()
_time()


# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        a = func(*args, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, round((end - start) * 1000, 2)))
        return a

    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
