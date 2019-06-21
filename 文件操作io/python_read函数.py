#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''

f = open("python_pathlib.py","r",True)
while True:
    # 每次读取一个字符
    ch = f.read(1)
    # 如果没有读到数据，跳出循环
    if not ch:
        break
    # 输出ch
    print(ch,end='')

f.close()

# 更安全的方式
try:
    while True:
        ch1 = f.read(1)
        if not ch1:
            break
        print(ch1,end='')
finally:
    f.close()
