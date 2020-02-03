# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: number_write.py
@time: 2020/2/3 10:55
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
import json

numbers=[2,3,5,7,9,11,13]

filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)