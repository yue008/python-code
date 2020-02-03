# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: amusemment_park.py
@time: 2020/2/1 15:46
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')


age=12
if age<4:
    print('You admission cost is $0.')
elif age < 18:
    print('Yoour admission cost is $5.')
else:
    print('Your admission cost is $10')
