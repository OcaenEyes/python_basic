#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''
import sqlite3
# 打开／创建数据库
conn = sqlite3.connect('first.db')
# 获取游标
c = conn.cursor()
# 执行DDL语句创建数据库
c.execute(
    '''
      CREATE TABLE user_tb(
        _id integer PRIMARY KEY AUTOINCREMENT ,
        name text,
        password text,
        gender text
      )  
    '''
)

c.execute(
    '''
      CREATE  TABLE order_tb(
        _id integer PRIMARY KEY AUTOINCREMENT ,
        item_name text,
        item_price real,
        item_number real,
        user_id integer,
        FOREIGN KEY (user_id) REFERENCES user_tb(_id)
      )
    '''
)

# 关闭游标
c.close()
# 关闭连接
conn.close()