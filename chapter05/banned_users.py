# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: banned_users.py
@time: 2020/2/1 15:41
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(user.title()+',you can post a response if you wish.')
