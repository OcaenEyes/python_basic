#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190624
    version:0.1.0
'''
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]

# 指定折线的颜色，线宽，样式
ln1, = plt.plot(x_data,y_data,color='red',linewidth=2.0,linestyle='--')
ln2, = plt.plot(x_data,y_data2,color='blue',linewidth=4.0,linestyle='-.')

# 调用legend函数添加图例
plt.legend(handles=[ln2,ln1],labels=['Android','Java'],loc='lower right')
'''  
    'best'：自动选择最佳位置。
    'upper right'：将图例放在右上角。
    'upper left'：将图例放在左上角。
    'lower left'：将图例放在左下角。
    'lower right'：将图例放在右下角。
    'right'：将图例放在右边。
    'center left'：将图例放在左边居中的位置。
    'center right'：将图例放在右边居中的位置。
    'lower center'：将图例放在底部居中的位置。
    'upper center'：将图例放在顶部居中的位置。
    'center'：将图例放在中心。
'''
plt.show()