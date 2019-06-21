#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import fileinput

# 可以拼接多个文件

# 一次读取多个文件
for line in fileinput.input(files=('python_for循环读取文件.py','python_open函数.py')):
    # 输出文件名，当前行在当前文件中的行号
    print(fileinput.filename(),fileinput.filelineno(),line,end='')

# 关闭文件流
fileinput.close()