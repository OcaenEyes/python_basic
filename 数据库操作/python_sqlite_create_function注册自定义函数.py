#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''
import sqlite3

'''
    create_function 方法包含 3 个参数：
        name 参数：指定注册的自定义函数的名字
        num_params：指定自定义函数所需参数的个数
        func：指定自定义函数对应的函数
'''
# 定义一个普通函数，准备注册为SQL中的自定义函数
def reverse_ext(st):
    # 对字符串反转，前后加括号
    return '['+ st[::-1] +']'

# 连接数据库
conn = sqlite3.connect('first.db')
# 调用create_function 注册自定义函数,enc
conn.create_function('enc',1,reverse_ext)
# 获取游标
c =conn.cursor()
# 在SQL语句中使用enc自定义函数
c.execute(
    'insert into user_tb values(null, ?, enc(?), ?)',
    ('贾宝玉', '123456', 'male')
)
conn.commit()
c.close()
conn.close()