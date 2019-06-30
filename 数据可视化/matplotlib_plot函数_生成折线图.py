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
y_data2 = [5200, 5420, 5150,5830, 5680, 5950, 6270]
# plt.plot(x_data,y_data)
# plt.plot(y_data)
# 传入了两组分别代表 X 轴、Y 轴数据的 list 列表
# plt.plot(x_data,y_data,x_data,y_data2)
# 多次调用 plot() 函数来生成多条折线
# plt.plot(x_data,y_data)
# plt.plot(x_data,y_data2)
# 传入额外的参数来指定折线的样子，如线宽、颜色、样式
'''
    -：代表实线，这是默认值。
    --：代表虚线。
    ·：代表点钱。
    -.：代表短线、点相间的虚钱。
'''
plt.plot(x_data,y_data, color='red',linewidth=2.0,linestyle='--')
plt.plot(x_data,y_data2,color='blue',linewidth=3.0,linestyle='-.')
plt.show()