# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: exercise4-6.py
@time: 2020/2/1 14:35
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print("python版本:\n" + sys.version)
print("--------------------------\n")

num=[]
for value in range(1,21,2):
    print(value)
    num.append(value)
print(num)