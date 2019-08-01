#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'字符流和字节流'
__author__ = 'ycn'

from io import BytesIO
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
from io import StringIO

si = StringIO()
si.write('hello')
si.write(' ')
si.write('world!')
print(si.getvalue())

# 读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
sir = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = sir.readline()
    if s == '':
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
bi = BytesIO()
bi.write('中文'.encode('utf-8'))
print(bi.getvalue())
# 小结
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
