#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import time
# print([e for e in dir(time) if not e.startswith('_')])
l= []
for e in dir(time):
    if not e.startswith('_'):
        l.append(e)
print(l)

# 将当前时间转换为时间字符串
print(time.asctime())

# 将指定时间转为时间字符串，时间元组的后面3个元素没有设置
print(time.asctime((2019,6,19,14,49,23,0,0,0)))

# 以秒数为代表的时间转换为时间字符串
print(time.ctime(30))

# 以秒数为代表的时间转换为struct_time对象
print(time.gmtime(30))

# 将当前时间转换为struct_time对象
print(time.gmtime())

# 以秒数为代表的时间转换为 代表当前时间的sruct_time对象
print(time.localtime(30))

# 返回性能计数器的值
print(time.perf_counter())

# 返回当前进程的cpu时间
print(time.process_time())