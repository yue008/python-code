# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: write_message.py
@time: 2020/2/2 20:28
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')


filename='programing.txt'

with open(filename,'w')as file_object:
    file_object.write('I love programing\n')
    file_object.write('l love creating new grames.\n')

with open(filename,'a') as file_object:
    file_object.write('I also love finding meaning in large datasets')
    file_object.write('I love creating apps that can run in brower')