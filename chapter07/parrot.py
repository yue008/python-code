# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: parrot.py
@time: 2020/2/2 8:29
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

prompt='\nTell me something,and I will repet it back to you:'
prompt+='\nEnter \'quit\' to end the program.\n'
message=''
while message!='quit':
    message=input(prompt)
    print(message)