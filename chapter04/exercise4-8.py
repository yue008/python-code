# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: exercise4-8.py
@time: 2020/2/1 14:39
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print("python版本:\n" + sys.version)
print("--------------------------\n")

nums=[]
for value in range(1,11):
    num=value**3
    print(num)
    nums.append(num)
print(nums)

