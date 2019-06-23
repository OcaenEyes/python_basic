#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''
import sqlite3
# fetchone() 用于获取一条记录，
# fetchmany(n) 用于获取 n 条记录，
# fetchall() 用于获取全部记录
conn = sqlite3.connect('first.db')
c =conn.cursor()
# 调用select查询
c.execute(
    'SELECT * FROM user_tb WHERE _id > ?',
    (2,)
)
print('查询返回的记录数',c.rowcount)
print(c.description)
# 通过游标的description属性获取列表信息
for col in (c.description):
    print(col[0],end='\t')
print('\n------------------')

# while True:
#     # 获取一行记录，每行数据是一个元组
#     row = c.fetchone()
#     # 如果抓取的row为None,退出循环
#     if not row:
#         break
#     print(row)
#     print(row[1] + '-->' + row[2])



while True:
    # 每次抓取3条记录，该方法返回一个由3条记录组成的列表
    rows = c.fetchmany(3)
    print('一次匹配3行',rows)
    # 如果抓取的rows为None，退出循环
    if not rows:
        break
    # 再次使用循环遍历获取的列表
    for r in rows:
        print('3行中每一行是',r)


c.close()
conn.close()

