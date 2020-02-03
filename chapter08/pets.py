# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: pets.py
@time: 2020/2/2 8:57
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print('\nI have a '+animal_type+'.')
    print('My '+ animal_type+'\'s name is '+pet_name.title()+'.')

describe_pet('hamster','harry')
describe_pet('dog','willie')