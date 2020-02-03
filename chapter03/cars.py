# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: cars.py
@time: 2020/2/1 13:30
@contact:python初学者(微信公众号)
--------------------- 
'''
import sys
print("python版本:\n"+sys.version)
print("--------------------------\n")

#按照字母顺序排序,永久性
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
#反向排序
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)


#sorted，临时性
cars=['bmw','audi','toyato','subaru']

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

#倒着打印列表,永久性
cars=['bmw','audi','toyato','subaru']
print(cars)
cars.reverse()
print(cars)

#确定列表长度,列表元素个数
cars=['bmw','audi','toyato','subaru']
print(len(cars))