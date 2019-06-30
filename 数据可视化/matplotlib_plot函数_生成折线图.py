#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190624
    version:0.1.0
'''
import matplotlib.pyplot as plt

# 定义两个列表作为X轴，Y轴数据
x_data = ['2013','2014','2015','2016','2017','2018','2019']

y_data = [5800,6020,6300,7100,8400,9050,10700]
# 第一个列表作为横坐标值，第二个列表作为纵坐标值
plt.plot(x_data,y_data)
plt.show()