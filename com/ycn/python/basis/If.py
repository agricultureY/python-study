#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ##########  条件判断  ###########
age = 20
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
x = 0
if x:
    print('not zero')
else:
    print('zero')
birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并打印BMI指数
# 低于18.5：过轻,18.5-25：正常,25-28：过重,28-32：肥胖,高于32：严重肥胖
bmi = 80.5 / (1.75 * 1.75)
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
