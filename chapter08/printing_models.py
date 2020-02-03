# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: printing_models.py
@time: 2020/2/2 9:33
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

#模拟打印每个设计，知道没有未打印的设计为止
#打印每个设计后，都将其移动到列表completed_models中
while unprinted_designs:
    current_design=unprinted_designs.pop()

    #模拟根据设计制作3D打印模型的过程
    print('Printing model: '+current_design)
    completed_models.append(current_design)

#显示打印好的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model)