# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: foods.py
@time: 2020/2/1 14:52
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print("python版本:\n" + sys.version)
print("--------------------------\n")

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)

print('\nMy favorite foods are:')
print(friend_foods)