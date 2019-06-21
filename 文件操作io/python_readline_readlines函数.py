#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import codecs

# 指定使用utf-8字符集读取文件
f = codecs.open("python_pathlib.py",'r','utf-8',buffering=True)

while True:
    # 每次一行,逐行读取
    line = f.readline()
    # 如果没有读到数据，跳出循环
    if not line:
        break

    # 输出line
    print(line,end='')

f.close()