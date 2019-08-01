#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'序列化'
__author__ = 'ycn'

import json
import pickle

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。
dic = dict(name='jack', age=24, sex='girl')
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
print(pickle.dumps(dic))
# pickle.dump()直接把对象序列化后写入一个file-like Object
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
with open('D:/ycn/Python/codes/test.txt', 'wb') as tf:
    pickle.dump(dic, tf)
with open('D:/ycn/Python/codes/test.txt', 'rb') as tf:
    print(pickle.load(tf))
print('==========================================================')

# 把Python对象变成一个JSON字符串
print(json.dumps(dic))
# 直接把Python转为json字符串并写入文件
with open('D:/ycn/Python/codes/test.json', 'w') as tf:
    json.dump(dic, tf)

# JSON反序列化为Python对象，loads()把JSON的字符串反序列化，
jsonStr = '{"age": 20, "score": 88, "name": "Bob"}'
print(type(json.loads(jsonStr)))
# load()方法从file-like Object中读取字符串并反序列化
with open('D:/ycn/Python/codes/test.json', 'r') as tf:
    print(json.load(tf))
print('==========================================================')


# 序列化class对象
# Python的dict对象可以直接序列化为JSON的{};默认情况下，dumps()方法不知道如何将class实例变为一个JSON的{}对象
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def stu2Dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }


s = Student('Bob', 20, 88)
print(json.dumps(s, default=stu2Dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))


# JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例
def json2Stu(d):
    return Student(d['name'], d['age'], d['score'])


stuJson = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(stuJson, object_hook=json2Stu))
