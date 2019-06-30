#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190624
    version:0.1.0
'''
from .say_hello import say_hello

def main():
    print("程序运行")
    print(say_hello('gzy'))


'''
指定将当前目录下的 app 子目录下的所有 Python 源文件打包成一个档案包，并通过 -o 选项指定所生成的档案包的文件名为 first.pyz；-m 选项指定使用 app.py 模块中的 main 函数作为程序入口
'''

if __name__ == '__main__':
    main()