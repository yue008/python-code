# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: name_function.py
@time: 2020/2/3 11:30
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def get_formatted_name(first,last):
    '''Generate a neatly formatted full name.'''
    full_name=first + ' '+last
    return full_name.title()