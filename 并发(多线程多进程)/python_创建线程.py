#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190623
    version:0.1.0
'''

'''
        1、使用threading模块的Thread类的构造器创建线程
        2、继承threading模块的Thread类创建线程类
'''

import threading
# 定义action函数，该函数准备作为线程执行体
def action(max):
    for i in range(max):
        # 调用threading 模块的current_thread()函数获取当前线程
        # 线程对象的getName()方法获取当前线程的名字
        print(threading.current_thread().getName() + ' ' + str(i))


# 主程序执行体
for j in range(100):
    print(threading.current_thread().getName() + ' ' + str(j))

    if j == 20:
        # 创建并启动第一个线程
        t1 = threading.Thread(target=action,args=(100,))
        t1.start()

        t2 = threading.Thread(target=action,args=(100,))
        t2.start()

print("主线程执行结束")
