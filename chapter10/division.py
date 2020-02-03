# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: division.py
@time: 2020/2/2 20:46
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')


try:
    print(5/0)
except ZeroDivisionError:
    print('You can\'t diveide by zero')

print('Give me two numbers,and I\'ll divide them:')
print('Enter \'q\' to quit')

while True:
    first_number=input('\nFirst umber:')
    if first_number=='q':
        break
    second_number=input('Second number:')
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    else:
        print(answer)