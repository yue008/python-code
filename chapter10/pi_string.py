# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: pi_string.py
@time: 2020/2/2 20:01
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
filename='pi_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))

