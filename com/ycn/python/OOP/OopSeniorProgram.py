#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'面向对象高级编程'
__author__ = 'ycn'

from enum import Enum, unique
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
print('=============================================')


############ @property绑定属性 ##############
class StudentSetter(object):
    _score = 0

    def getScore(self):
        return self._score

    def setScore(self, val):
        if not isinstance(val, int):
            raise ValueError("score must be an integer...")
        if val < 0 or val > 100:
            raise ValueError("score must between 1 and 100...")
        self._score = val


ss1 = StudentSetter()
# ss1.setScore(999)
ss1.setScore(60)
print(ss1.getScore())
print('=============================================')


# @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
# 只定义getter方法，不定义setter方法就是一个只读属性
# 于是，我们就拥有一个可控的属性操作
class StudentProperty:
    _score = None
    _birth = None
    _age = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError("score must be an integer...")
        if val < 0 or val > 100:
            raise ValueError("score must between 1 and 100...")
        self._score = val

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, val):
        self._birth = val

    @property
    def age(self):
        return 2019 - self._birth


sp1 = StudentProperty()
sp1.score = 80
# sp1.score = 999
print(sp1.score, '--------', sp1._score)
# sp1.age = 12      can't set attribute
sp1.birth = 1996
print(sp1.birth, '----------', sp1.age)
print('=============================================')


# 小结
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
# 这样，程序运行时就减少了出错的可能性。


############# 多重继承  一个子类就可以同时获得多个父类的所有功能 ##############
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。


############### 定制类 ##################
class CustomClass:
    def __init__(self, name):
        self.name = name
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __str__(self):
        return 'custom object (name : %s)' % self.name

    # 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
    # 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__ = __str__

    # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
    # 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    # 直到遇到StopIteration错误时退出循环。
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个
        if self.a > 10:
            raise StopIteration()
        return self.a  # 返回下一个值

    # 像list那样按照下标取出元素，需要实现__getitem__()方法
    # 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
    # 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
    # 最后，还有一个__delitem__()方法，用于删除某个元素。
    def __getitem__(self, item):
        if isinstance(item, int):  # item是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    # 当调用对象属性不存在时，Getattr()方法，动态返回一个属性。
    # 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，不会在__getattr__中查找
    def __getattr__(self, attr):
        if attr == 'score':
            return 0  # 返回数字
        if attr == 'age':
            return lambda: 25  # 返回函数
        raise AttributeError("custom object has not attribute '%s'" % attr)

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
    # 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，
    # 因为这两者之间本来就没啥根本的区别。
    # 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，
    # 这么一来，我们就模糊了对象和函数的界限。
    # 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
    # 能被调用的对象就是一个Callable对象
    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)


cus = CustomClass('jack')
print(cus)
for n in cus:
    print(n)
print('cus index 4 -->', cus[4])
print('cus slice  1-5 -->', cus[1:5])
print('cus without score:', cus.score)
print('cus without age:', cus.age())
# print('cus without birth:', cus.birth)
cus()
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(cus))
print(callable('123'))
print(callable(max))
print('=============================================')


class Rest:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Rest('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Rest().status.user.timeline.list)
print('=============================================')

############# 枚举类 #################
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(WeekDay.Sun.name, '---', WeekDay.Sun.value)
print(WeekDay['Fri'].name, '---', WeekDay['Fri'].value)
print(WeekDay(2).name, '---', WeekDay(2).value)
print('=============================================')


################# 元类 #####################
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，
# 而无需通过class Hello(object)...的定义。

# 定义函数
def helloFn(self, name='world'):
    print('hello, %s' % name)


Hello = type('Hello', (object,), dict(hello=helloFn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
# 要创建一个class对象，type()函数依次传入3个参数：
#   1、class的名称；
#   2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#   3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，
# 本质上都是动态编译，会非常复杂。

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# metaclass可以给我们自定义的MyList增加一个add方法：
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass