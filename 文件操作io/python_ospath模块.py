#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import os
import time

# 获取绝对路径
print(os.path.abspath("python_pathlib.py"))

# 获取共同前缀
print(os.path.commonprefix(['/usr/lib','/usr/local/lib']))

# 获取共同路径
print(os.path.commonpath(['/usr/lib','/usr/local/lib']))

# 获取目录
print(os.path.dirname('gzy/gzy/1.txt'))

# 判断目录是否存在
print(os.path.exists('gzy/gzy/1.txt'))

# 获取最近一次访问时间
print(time.ctime(os.path.getatime("python_pathlib.py")))

# 获取最近一次修改时间
print(time.ctime(os.path.getmtime("python_pathlib.py")))

# 获取创建时间
print(time.ctime(os.path.getctime("python_pathlib.py")))

# 获取文件大小
print(os.path.isfile("python_pathlib.py"))

# 判断是否为目录
print(os.path.isdir("python_pathlib.py"))

# 判断是否为同一个文件
print(os.path.samefile('python_pathlib.py','./python_pathlib.py'))