#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'类和实例'

__author__ = 'ycn'


# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
# 比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 仍以Student类为例，在Python中，定义类是通过class关键字
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    pass


# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
bart = Student()
print(bart)
print(Student)
# 变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
# 可以自由地给一个实例变量绑定属性
bart.name = 'Bart Simpson'
print(bart.name)


# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去(类似于java构造函数)
# 注意：特殊方法“__init__”前后分别有两个下划线！！！
class StudentAttr(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
# 就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
bart = StudentAttr('Bart Simpson', 59)
print(bart.name, '<----->', bart.score)


# 数据封装
# 面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。
# 我们可以通过函数来访问这些数据，比如打印一个学生的成绩
# 但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
# 这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
# 这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，
# 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节
class StudentMethod(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printScore(self):
        print('%s : %s' % (self.name, self.score))

    def getGrade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = StudentMethod('Bart Simpson', 74)
bart.printScore()
print(bart.getGrade())


# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class StudentPrivate(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def printScore(self):
        print('%s : %s' % (self.__name, self.__score))


bart = StudentPrivate('Bart Simpson', 59)
# bart.__name
bart.printScore()
# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_StudentPrivate__name，所以，仍然可以通过_StudentPrivate__name来访问__name变量
print(bart._StudentPrivate__name)

# 小结
# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，
# 但拥有的变量名称都可能不同
