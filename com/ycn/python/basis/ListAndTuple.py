#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  list和tuple  ###########
# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['张三', '李四', '王五', '赵六']
print(classmates)
print(len(classmates))
print(classmates[1])
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素，以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-1])
print(classmates[-3])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('田七')
print(classmates)
# 也可以把元素插入到指定的位置，比如索引号为2的位置
classmates.insert(2, '胡八')
print(classmates)
# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(2)
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = '胡八'
print(classmates)
# list里面的元素的数据类型也可以不同
typeDiffList = ['str', 1, 2, 3]
print(typeDiffList)
# list元素也可以是另一个list
anotherList = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(anotherList), '->', anotherList)

# tuple
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('张三', '李四', '王五', '赵六')
print(classmates)
print(classmates[2])
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。当你定义一个tuple时，tuple的元素就必须被确定下来
# 但是，要定义一个只有1个元素的tuple，如果你这么定义：t = (1)，定义的不是tuple，是1这个数！
# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1)
print(t)
t = (1,)
print(t)
# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2].append('C')
print(t)
