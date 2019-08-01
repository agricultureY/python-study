#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'文件读写'
__author__ = 'ycn'
# 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
try:
    # 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
    file = open('D:/ycn/Python/codes/test.txt', 'r')
    # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    print(file.read())
except IOError as e:
    print(e)
finally:
    if file:
        # 调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
        file.close()
# Python引入了with语句来自动帮我们调用close()方法
with open('D:/ycn/Python/codes/test.txt', 'r') as tf:
    print(tf.read())
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('D:/ycn/Python/codes/test.txt', 'r') as tf:
    for line in tf.readlines():
        print(line)
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('D:/ycn/life/images/head01.jpg', 'rb') as img:
    print(img.read())
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，errors参数，表示如果遇到编码错误后如
with open('D:/ycn/Python/codes/test.txt', 'r', encoding='gbk', errors='ignore') as tf:
    print(tf.read())

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# r --> open for reading (default)
# w --> open for writing, truncating the file first
# x --> open for exclusive creation, failing if the file already exists
# a --> open for writing, appending to the end of the file if it exists
# b --> binary mode
# t --> text mode (default)
# + --> open a disk file for updating (reading and writing)
with open('D:/ycn/Python/codes/test.txt', 'a') as tf:
    tf.write('\r\n哒哒哒哒')

