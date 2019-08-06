#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ycn'

from datetime import datetime, timedelta, timezone

# datetime是Python处理日期和时间的标准库。
# 获取当前日期和时间
now = datetime.now()
print(now, '-------->', type(now))

# 获取指定日期和时间
dt = datetime(2019, 8, 1, 12, 12)
print(dt)

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print(now.timestamp())

# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
t = 1564732704.0
print(datetime.fromtimestamp(t))  # 本地时间
print(datetime.utcfromtimestamp(t))  # utc时间

# str转换为datetime
# 通过datetime.strptime()实现str转换为datetime，需要一个日期和时间的格式化字符串
cday = datetime.strptime('2019-8-1 12:22:59', '%Y-%m-%d %H:%M:%S')
print(cday, '------------>', type(cday))

# 通过strftime()实现datetime转换为str
print(now.strftime('%Y-%m-%d %H:%M:%S'))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
print(now + timedelta(days=1, hours=1))
print(now - timedelta(days=1))

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dt)

# 时区转换
# 通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
