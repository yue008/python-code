# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: counting.py
@time: 2020/2/2 8:28
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1

current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)