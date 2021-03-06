#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import os

#显示导入依赖模块的操作系统名称
print(os.name)

# 获取PYTHONPATH环境变量的值
print(os.getenv('PYTHONPATH'))

# 返回当前系统的登录用户名
print(os.getlogin())

# 获取当前进程id
print(os.getpid())

# 获取当前进程的父进程id
print(os.getppid())

# 返回当前系统的CPU数量
print(os.cpu_count())

# 返回路径分隔符
print(os.sep)

# 返回当前系统的路径分隔符
print(os.pathsep)

# 返回当前系统的换行符
print(os.linesep)

# 返回适合作为加密使用的，最多3个字节组成的bytes
print(os.urandom(3))