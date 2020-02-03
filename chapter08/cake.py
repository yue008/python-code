# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: cake.py
@time: 2020/2/2 9:58
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
# import sys
#
# print('本程序在python3.7.3编译，运行时请注意python版本')
# print('python当前版本:\n' + sys.version)
# print('--------------------------\n')

#此程序和原文的pizza一样
def  make_cake(size,*toppings):
    '''概述要制作的蛋糕'''
    print('\nMaking a '+ str(size)+
          '-inch cake with the following toppings:')
    for topping in toppings:
        print('-'+topping)