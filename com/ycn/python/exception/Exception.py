#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'异常处理'
__author__ = 'ycn'

import logging
import unittest

from MyDict import Dict

logging.basicConfig(level=logging.INFO)

# try...except...finally...的错误处理
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
print('=============================')

# 抛出异常
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。
# 因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
try:
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')
except ValueError as e:
    print(e)
print('=============================')

# 断言
# 启动Python解释器时可以用-O参数来关闭assert
n = 3
assert n != 0, 'n is zero'

# logging允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
s = '0'
n = int(s)
logging.info('n = %d' % n)


# print(10 / n)

# pdb，让程序以单步方式运行，可以随时查看运行状态。
# python -m pdb err.py

############# 单元测试 ################
# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
# 这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。
# 在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，
# 我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
class TestDict(unittest.TestCase):

    def test_init(self):
        print('test_init...')
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        print('test_key...')
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        print('test_attr...')
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        print('test_keyerror')
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        print('test_attrerror')
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# 运行单元测试
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()


# 这样就可以把mydict_test.py当做正常的python脚本运行：$ python mydict_test.py
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：$ python -m unittest mydict_test
# 小结
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

############# 文档测试 ###############
# 自动执行注释中的代码，然后由工具生成文档
# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
# 只有测试异常的时候，可以用...表示中间一大段烦人的输出。
def abs(n):
    """
    :param n:
    :return:
    Function to get absolute value of number.
    Example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n >= 0 else (-n)
