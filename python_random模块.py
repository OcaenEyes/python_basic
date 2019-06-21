#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190619
    version:0.1.0
'''
import random
# 生成伪随机数

print(random.__all__)

# 生成范围为0.0 <= x <= 1.0的伪随机浮点数
print(random.random())

# 生成范围为2。5 <= x <= 10.0的伪随机浮点数
print(random.uniform(2.5,10.0))

# 生成 呈指数分布的伪随机数
print(random.expovariate(1/5))

# 生成从0到9 的伪随机整数
print(random.randrange(10))

# 生成从0到100的随机偶数
print(random.randrange(0,101,2))

# 随机抽取一个元素
print(random.choice(['python','swift','flutter']))

# 对列表元素进行随机排列
book_list = ['python','swift','flutter']
random.shuffle(book_list)
print(book_list)

#随机抽取4个独立的元素
print(random.sample([10,20,30,40,50],k=4))
