# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: scatter_squares.py
@time: 2020/2/5 16:44
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)

#设置图标标题并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Squares of Values',fontsize=14)

#保存文件
#plt.savefig('Squares_plot.png',bbox_inches='tight')

#设置刻度标记的大小
plt.axis([0,1100,0,1100000])

plt.show()
