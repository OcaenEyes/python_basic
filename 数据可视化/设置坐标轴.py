#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    auth:gzy
    date:20190624
    version:0.1.0
'''
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
my_font = FontProperties(fname="../SourceHanSans-Normal.otf")
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color = 'red', linewidth = 2.0,
    linestyle = '--', label='Java基础')
plt.plot(x_data, y_data2, color = 'blue', linewidth = 3.0,
    linestyle = '-.', label='C基础')
plt.legend(loc='best')
plt.xlabel('年份',fontproperties=my_font)
plt.ylabel('教程销量',fontproperties=my_font)
plt.title('C语言中文网的历史销量',fontproperties=my_font)
plt.yticks([50000, 70000, 100000],['挺好', '优秀', '火爆'],fontproperties=my_font)
plt.show()