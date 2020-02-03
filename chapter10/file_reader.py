# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: file_reader.py
@time: 2020/2/2 19:38
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

# with open('pi_digits.txt') as file_object:
#     contents=file_object.read()
#     print(contents.rstrip())

filename='pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
