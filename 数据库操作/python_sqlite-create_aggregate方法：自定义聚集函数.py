#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''
import sqlite3

'''
create_aggregate 方法包含 3 个参数：

    name：指定自定义聚集函数的名字。
    num_params：指定聚集函数所需的参数。
    aggregate_class：指定聚集函数的实现类。该类必须实现 step(self, params...) 和 finalize(self) 方法，其中 step() 方法对于查询所返回的每条记录各执行一次；finalize(self) 方法只在最后执行一次，该方法的返回值将作为聚集函数最后的返回值。

'''
# 定义一个普通类, 竹本注册为sql的自定义聚集函数
class MinLen():
    def __init__(self):
        self.min_len = None

    def step(self,value):
        # 如果self.min_len还未赋值，则将当前value赋值给self.min_len
        if self.min_len is None:
            self.min_len = value
            return

        # 找到一个长度更短的value ,用value代替self.min_len
        if len(self.min_len) > len(value):
            self.min_len = value

    def finalize(self):
        return self.min_len

# 打开/创建数据库
conn = sqlite3.connect('first.db')
# 调用create_aggregate 住粗自定义聚集函数 min_len
conn.create_aggregate('min_len',1,MinLen)
#获取游标
c = conn.cursor()
c.execute(
    'SELECT min_len(password) FROM user_tb'
)
print(c.fetchone()[0])

conn.commit()
c.close()
conn.close()

