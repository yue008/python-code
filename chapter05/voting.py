# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: voting.py
@time: 2020/2/1 15:43
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

age =17
if age>= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry,you are too young to vote')
    print('Please register to vote as soons as you turn 18!')
