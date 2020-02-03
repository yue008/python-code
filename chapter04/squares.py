# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: squares.py
@time: 2020/2/1 13:48
@contact:python初学者(微信公众号)
--------------------- 
'''
import sys
print("python版本:\n"+sys.version)
print("--------------------------\n")

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)

#列解析
squares=[value**2 for value in range(1,11)]
print(squares)
