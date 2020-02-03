# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: even_or_odd.py
@time: 2020/2/2 8:25
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

number=input('Enter a number,and I\'ll tell you if it\'s even or odd:')
number=int(number)

if number%2==0:
    print('\nThe number '+str(number)+' is even')
else:
    print('\nThe number '+str(number)+' is odd')
