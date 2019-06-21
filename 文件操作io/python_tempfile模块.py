#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''

import tempfile
# 临时文件

# 创建临时文件
fp = tempfile.TemporaryFile()
print(fp.name)

fp.write('人生若只如初见'.encode('utf-8'))
fp.write('何事秋风悲画扇'.encode('utf-8'))

# 将文件指针移动到开始处，准备读取文件
fp.seek(0)
print(fp.read().decode('utf-8'))
# 关闭文件，该文件将会被自动删除
fp.close()


# 通过with创建临时文件，with会自动关闭临时文件
with tempfile.TemporaryFile() as fp1:
    # 写入内容
    fp1.write(b'ysilhouette')
    # 将文件指针移到开始处,准备读取文件
    fp1.seek(0)
    # 读取文件内容
    print(fp1.read())


# with创建临时文件夹
with tempfile.TemporaryDirectory() as tmpdir:
    print("创建临时文件夹",tmpdir)