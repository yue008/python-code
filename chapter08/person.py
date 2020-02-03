# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: person.py
@time: 2020/2/2 9:07
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def build_person(first_name,last_name,age=''):
    '''返回一个字典，其中包含有关一个人的信息'''
    person={'first':first_name,
            'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)
