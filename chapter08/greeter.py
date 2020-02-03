# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: greeter.py
@time: 2020/2/2 8:54
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def greet_user():
    '''显示简单的问候语'''
    print('Hello')

greet_user()

def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name=first_name+' '+last_name
    return full_name

#这是一个无限循环
while True:
    print('\nPlease tell me your name:')
    print('(enter \'q\' at any time to quit)')
    f_name=input('First name:')
    if f_name=='q':
        break
    l_name=input('Last name:')
    if l_name=='q':
        break

    formatted_name=get_formatted_name(f_name,l_name)
    print('\nHello,'+formatted_name+'!')