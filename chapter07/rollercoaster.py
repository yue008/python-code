# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: rollercoaster.py
@time: 2020/2/2 8:22
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

height=input('How tall are you,in inches?')
height=int(height)

if height>= 36:
    print('\nYou\'re tall enoough to ride!')
else:
    print('\nYou\'ll be able to ride when you\'re a little older')