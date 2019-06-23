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
        'INSERT INTO user_tb VALUES(null, ?, ?, ?)',
        ('gzy','123456','female')
    )
except Exception as e:
    print('user',e)

try:
    c.execute(
        'INSERT INTO order_tb VALUES(null, ?, ?, ?, ?)',
        ('AirPods','1246.1','1',1)
    )
except Exception as e:
    print('order',e)

# 使用 executemany() 重复执行 insert 语句
try:
    c.executemany(
        'INSERT INTO user_tb VALUES (null,?,?,?)',
        (('sun', '123456', 'male'),
         ('bai', '123456', 'female'),
         ('zhu', '123456', 'male'),
         ('niu', '123456', 'male'),
         ('tang', '123456', 'male'))
    )
except Exception as e:
    print(e)

# 使用 executemany() 重复执行 update 语句
try:
    c.executemany(
        'UPDATE user_tb SET name=? WHERE _id=?',
        (('小孙', 2),
        ('小白', 3),
        ('小猪', 4),
        ('小牛', 5),
        ('小唐', 6))
    )
except Exception as e:
    print(e)

conn.commit()

c.close()
conn.close()