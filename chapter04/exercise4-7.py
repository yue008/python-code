# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: exercise4-7.py
@time: 2020/2/1 14:37
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print("python版本:\n" + sys.version)
print("--------------------------\n")

num=[]
for value in range(3,31):
    if value%3==0:
        print(value)
        num.append(value)
print(num)
