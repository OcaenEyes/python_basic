#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''

'''
    w   只读模式
    r   写模式
    a   追加模式
    +   读写模式
    b   二进制模式
    
'''
# open()函数，打开指定文件
f = open("python_pathlib.py")
# 访问文件的编码方式
print(f.encoding)

# 访问文件的访问模式
print(f.mode)

# 访问文件是否已经关闭
print(f.closed)

# 访问文件对象打开的文件名
print(f.name)