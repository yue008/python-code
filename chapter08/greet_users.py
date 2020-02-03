# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: greet_users.py
@time: 2020/2/2 9:17
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def greet_users(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        msg='hello,'+name.title()+'!'
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)
