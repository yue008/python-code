# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: greet_user.py
@time: 2020/2/3 11:05
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
import json

filename='username.json'
with open(filename) as f_obj:
    username=json.load(f_obj)
    print('Welcome back,'+username+'!')
