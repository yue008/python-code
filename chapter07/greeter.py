# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: greeter.py
@time: 2020/2/2 8:18
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

# name=input('Please enter your name:')
# print('Hello,'+name+'!')

prompt='If you tell me who you are,we can personalize the message you see.'
prompt+='\nWhat is your first name?'

name=input(prompt)
print('\nHello,'+name+'!')
