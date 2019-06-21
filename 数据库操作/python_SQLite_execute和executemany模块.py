#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''

import sqlite3
conn = sqlite3.connect('first.db')
print('数据库连接成功')
c = conn.cursor()
print("创建游标成功")
try:
    c.execute(
        'INSERT INTO user_tb VALUES(null, ?, ?, ?)',('gzy','123456','female')
    )
    print("插入user成功")
except Exception as e:
    print('user',e)

try:
    c.execute(
        'INSERT INTO order_tb VALUES(null, ?, ?, ?, ?)',('AirPods','1246.1','1',1)
    )
    print("插入order成功")
except Exception as e:
    print('order',e)

c.close()
conn.close()