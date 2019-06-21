#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''

import os
# 获取当前的目录
print(os.getcwd())

# 改变当前目录
os.chdir('')

path = ''
# 创建目录
os.mkdir(path,0o777)
# 删除目录
os.rmdir(path,0o777)