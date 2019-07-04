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
print('<======================================================>')

#   ##########  生成器  ###########
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素。这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)
# 遍历生成器
for n in g:
    print(n)
print('<======================================================>')


# 生成斐波拉契数列(1, 1, 2, 3, 5, 8, 13, 21, 34, ...)
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(10)
print('<======================================================>')


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib_gen(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


fib_g = fib_gen(10)
print(fib_g)
for n in fib_g:
    print(n)
print('<======================================================>')


# generator和函数的执行流程不一样；函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(next(o))
print(next(o))
print(next(o))
