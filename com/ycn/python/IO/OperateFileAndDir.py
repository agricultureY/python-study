#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'操作文件和目录'
__author__ = 'ycn'

import os

# Python内置的os模块也可以直接调用操作系统提供的接口函数
print(os.name)  # 查看操作系统类型（posix-->Linux、Unix或Mac OS X，nt-->Windows系统）
# print(os.uname())  # 获取详细的系统信息(uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的)
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('APPDATA'))

# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
os.path.join('D:/ycn/Python', 'testdir')
# 然后创建一个目录
os.mkdir('D:/ycn/Python/testdir')
# 删除目录
os.rmdir('D:/ycn/Python/testdir')
# 拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('D:/ycn/Python/codes/test.txt'))
# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('D:/ycn/Python/codes/test.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

# 对文件进行重命名
os.rename('D:/ycn/Python/codes/test.txt', 'D:/ycn/Python/codes/test.py')
# 删除文件
os.remove('D:/ycn/Python/codes/test.py')

# 复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

# 过滤文件
print([x for x in os.listdir('D:/ycn') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
