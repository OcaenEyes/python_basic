#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''
import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()
# 调用executescript()执行SQL脚本
c.executescript(
    '''
        INSERT INTO user_tb VALUES (null,'wuda','12344','male');
        INSERT INTO user_tb VALUES (null,'wsad','12364','female');
    '''
)
conn.commit()
c.close()
conn.close()