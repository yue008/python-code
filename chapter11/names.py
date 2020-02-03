# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: names.py
@time: 2020/2/3 11:31
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

from name_function import get_formatted_name

print('Enter \'q\' at any time to quit.')
while True:
    first=input('\nPlease give me a first name:')
    if first=='q':
        break
    last=input('Please give me a last name:')
    if last=='q':
        break
    formatted_name=get_formatted_name(first,last)
    print('\nNeatly formatted name: '+formatted_name+'.')