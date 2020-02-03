# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: cities.py
@time: 2020/2/2 8:33
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
prompt='\nPlease enter the name of a coty you have wisited:'
prompt+='\n(Enter \'quit\' when you are finished.)'

while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print('I\'d love to go to '+city.title()+'!')