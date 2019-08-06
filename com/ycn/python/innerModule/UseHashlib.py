#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ycn'

import hashlib
import hmac

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 改动一个字母最后的计算结果都不一样
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())
print('================================================')

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
print('================================================')

# 可能两个不同的数据通过某个摘要算法得到了相同的摘要，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
# 这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
# 并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。

# Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
message = b'Hello, world!'
key = b'secret'
hm = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(hm.hexdigest())


# 小结
# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
# 只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
