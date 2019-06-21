#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
from pathlib import *
import fnmatch

'''
    * : 可匹配任意个任意字符
    ？ ： 可匹配一个任意字符
'''

# 遍历当前目录下所有文件和子目录
for file in Path('.').iterdir():
    # 访问所有以 .py结尾的文件
    if fnmatch.fnmatch(file,'*.py'):
        print(file)