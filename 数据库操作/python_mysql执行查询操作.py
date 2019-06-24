#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190623
    version:0.1.0
'''

# 导入访问mysql的模块
import pymysql

conn = pymysql.connect('127.0.0.1','root','123456','testdata')
c = conn.cursor()

c.execute(
    'SELECT * FROM user_tb WHERE user_id = %s',
    (1,)
)

for col in (c.description):
    print(col[0],end='\t')

print('\n')
while True:
    row = c.fetchone()
    if not row:
        break
    print(row)

c.close()
conn.close()