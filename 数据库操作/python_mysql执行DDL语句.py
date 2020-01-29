#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190623
    version:0.1.0
'''

# 导入访问mysql的模块
import pymysql
# 连接数据库
conn = pymysql.connect('127.0.0.1','root','123456','testdata')
# 获取游标
c = conn.cursor()
# 执行DDL语句创建数据表
c.execute(
    '''
        CREATE TABLE user_tb(
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255),
            password VARCHAR(255),
            gender VARCHAR(255)
        )
    '''
)
c.execute(
    '''
        CREATE TABLE order_tb(
            order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            item_name VARCHAR(255),
            item_price DOUBLE,
            item_number DOUBLE,
            user_id INT,
            FOREIGN KEY(user_id) REFERENCES user_tb(user_id)
        )
    '''
)

# 关闭游标
c.close()
conn.close()