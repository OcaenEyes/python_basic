#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190623
    version:0.1.0
'''

# 导入访问mysql的模块
import pymysql
# 使用游标的 execute() 方法执行 DML 的 insert、update、delete 语句，对数据库进行插入、修改和删除数据操作。

conn = pymysql.connect('127.0.0.1','root','','testdata')
c = conn.cursor()
c.execute(
    'insert into user_tb values(null, %s, %s, %s)',
    ('孙悟空', '123456', 'male')
)
c.execute(
    'insert into order_tb values(null, %s, %s, %s, %s)',
    ('鼠标', '34.2', '3', 1)
)
conn.commit()
# 关闭游标
c.close()
# 关闭连接
conn.close()