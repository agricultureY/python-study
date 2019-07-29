#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'继承和多态  获取对象信息  实例属性和类属性'

__author__ = 'ycn'

import types


################ 继承和多态 #################
# 当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）
class Animal(object):
    def run(self):
        print("animal is running ......")


# 定义继承animal
class Dog(Animal):
    pass


class Cat(Animal):
    # 重写父类方法
    def run(self):
        print("cat is running ......")

    def eat(self):
        print("cat is eating ......")


dog = Dog()
dog.run()
cat = Cat()
cat.run()
cat.eat()


# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。

def run_twice(animal):
    animal.run()


run_twice(Dog())
run_twice(Cat())

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
# 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思。
# 调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

# 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。


############ 获取对象信息 ################
# 我们来判断对象类型，使用type()函数：基本类型、函数、类都可以用type()判断
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(dog))


# 可以使用types模块中定义的常量判断一个对象是否是函数、lambda、迭代器
def fn():
    pass


print('======================================')
print(type(fn) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
class JinMao(Dog):
    def run(self):
        print('jin mao is running')


print('======================================')
jinMao = JinMao()
print(type(jinMao))
print(isinstance(jinMao, Animal))
print(isinstance(jinMao, Dog))
print(isinstance(jinMao, JinMao))
print(isinstance(dog, JinMao))
# isinstance()可以判断基本数据类型，也可以判断是否为多个数据类型中的一种
print(isinstance(123, int))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print('====================================')
# dir()可以获取一个对象的所有属性和方法
# 调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
print(dir('abc'))


# getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


myObject = MyObject()
print(hasattr(myObject, 'x'))  # myObject对象是否有x属性
print(hasattr(myObject, 'y'))  # myObject对象是否有y属性
setattr(myObject, 'y', 10)  # 设置一个y属性
print(hasattr(myObject, 'y'))  # myObject对象是否有y属性
print(getattr(myObject, 'y'))  # 获取y属性的值
print(myObject.y)
# 获取不存在的属性，会抛出AttributeError的错误，可以设置默认值，当属性不存在时，返回默认值
print(getattr(myObject, 'z', 404))
# 获取对象的方法
objFn = getattr(myObject, 'power')
print(objFn())


# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。

############### 实例属性和类属性 ##################
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性；给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    # 可以直接在class中定义属性，这种属性是类属性，归Student类所有
    name = 'student'

    def __init__(self, name):
        self.name = name


print(Student.name)
stu = Student('张三')
stu.score = 90
print(stu.name, '---->', stu.score)
# 删除实例对象属性
del stu.name
print(stu.name)
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 小结
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
