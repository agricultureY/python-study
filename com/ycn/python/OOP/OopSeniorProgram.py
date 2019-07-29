#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'面向对象高级编程'
__author__ = 'ycn'

from types import MethodType

################### __slots__限制类实例动态添加属性 #######################
# 当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student:
    pass


stu = Student()
stu.name = '张三'  # 给实例绑定属性
print(stu.name)


# 定义函数
def setAge(self, age):
    self.age = age


# 给实例绑定方法
stu.setAge = MethodType(setAge, stu)
stu.setAge(24)
print(stu.age)
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的，为了给所有实例都绑定方法，可以给class绑定方法
stu1 = Student()


# print(stu1.name)
# stu1.setAge(26)
# print(stu1.age)
def setScore(self, score):
    self.score = score


Student.setScore = setScore
stu.setScore(88)
stu1.setScore(66)
print(stu.score)
print(stu1.score)

print('=============================================')


# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


per1 = Person()
per1.name = '李四'
per1.age = 27
print(per1.name)
print(per1.age)
# per1.score = 86
# print(per1.score)
