#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  循环控制  ###########
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['张三', '李四', '王五', '赵六']
print(names)
for name in names:
    print(name)
# 循环求和
sumNum = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in nums:
    sumNum = sumNum + x
print(sumNum)
sumNum = 0
# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
nums = list(range(101))
for x in nums:
    sumNum = sumNum + x
print(sumNum)
sumNum = 0
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
n = 99
while n > 0:
    if n % 2 == 1:
        sumNum = sumNum + n
    n = n - 1
print(sumNum)
sumNum = 0
# 在循环中，break语句可以提前退出循环
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
