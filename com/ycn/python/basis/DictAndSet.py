#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  dict(map) and set  集合  ###########
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Adam'] = 67
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
# 如果key不存在，dict就会报错
# 通过in判断key是否存在
print('Tracy' in d)
print('tt' in d)
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
if not d.get('tt'):
    print('d not have')
print(d.get('Tracy', -1))
print(d.get('tt', -1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Tracy')
print('Tracy' in d)
# dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合，同时重复元素在set中会被过滤
l = [1, 2, 3, 2, 4, 5, 2, 3]
print(l)
s = set(l)
print(s)
# 通过add(key)方法可以添加元素到set中
s.add(6)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(2)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
