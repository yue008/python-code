# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: pizza.py
@time: 2020/2/2 9:41
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')


def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print('\nMaking a pizza with the following topping:')
    for topping in toppings:
        print('-'+topping)

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
