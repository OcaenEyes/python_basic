#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import sys
# print([e for e in dir(sys) if not e.startswith('_')])
l= []
for e in dir(sys):
    if not e.startswith('_'):
        l.append(e)
print(l)

# 显示本地字节序的指示符
print(sys.byteorder)

# 显示python解释器有关的版权信息
print(sys.copyright)

# 显示解释器在磁盘上的存储路径
print(sys.executable)

# 显示当前系统上保存文件所使用的字符集
print(sys.getfilesystemencoding())

# 显示python整数支持的最大值
print(sys.maxsize)

# 显示解释器所在的平台
print(sys.platform)

# 显示当前python解释器的版本信息
print(sys.version)
