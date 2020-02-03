# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: pizz.py
@time: 2020/2/1 17:58
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

#存储所点批萨的信息
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
#概述所点的比萨
print('You ordered a '+pizza['crust']+'-crust pizza '+ 'with the following toppings:')
for topping in pizza['toppings']:
    print('\t'+topping)