#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190623
    version:0.1.0
'''
import threading
'''
    线程的生命周期:
        新建 new
        就绪 ready
        运行 running
        阻塞 blocked
        死亡 dead
'''
##### 线程的新建和就绪状态
# 启动线程使用start()方法；系统将run()方法当线程执行体来处理

# 定义准备作为线程执行体的action函数
def action(max):
    for i in range(max):
        # 直接调用run()方法，Thread的name属性返回的是该对象的名字
        # 而不是当前线程的名字
        # 使用threading.current_thread().name 获取当前线程的名字
        print(threading.current_thread().name + ' ' +str(i))

for j in range(100):
    # 调用Thread的current_thread()方法获取当前线程
    print(threading.current_thread().name + ' ' + str(j) )
    if j == 20:
        # 直接调用线程对象的run()方法
        # 系统把线程对象当成普通对象，把run()方法当成普通方法
        # 不启动两个线程， 而是依次执行两个run()方法
        threading.Thread(target=action,args=(100,)).run()
        threading.Thread(target=action,args=(100,)).run()

###### 线程的运行和阻塞状态


###### 线程死亡
