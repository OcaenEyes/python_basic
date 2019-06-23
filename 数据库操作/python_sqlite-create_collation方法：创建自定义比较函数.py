#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190620
    version:0.1.0
'''
import sqlite3
'''
    create_collation 方法包含两个参数：

        name：指定自定义比较函数的名字。
        callable：指定自定义比较函数对应的函数。该函数包含两个参数，并对这两个参数进行大小比较，如果该方法返回正整数，系统认为第一个参数更大；如果返回负整数，系统认为第二个参数更大；如果返回 0，系统认为两个参数相等。

'''
# 去掉字符串第一个、最后一个字符后比较大小
def my_collate(st1, st2):
    if st1[1: -1] == st2[1: -1]:
        return 0
    elif st1[1: -1] > st2[1: -1]:
        return 1
    else:
        return -1
# ①、打开或创建数据库
# 也可以使用特殊名：:memory:代表创建内存中的数据库
conn = sqlite3.connect('first.db')
# 调用create_collation注册自定义比较函数：sub_cmp
conn.create_collation('sub_cmp', my_collate)
# ②、获取游标
c = conn.cursor()
# ③、在SQL语句中使用sub_cmp自定义的比较函数
c.execute('select * from user_tb order by password collate sub_cmp')
# 采用for循环遍历游标
for row in c:
    print(row)
conn.commit()
# ④、关闭游标
c.close()
# ⑤、关闭连接
conn.close()