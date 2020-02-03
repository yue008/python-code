# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: formatted_name.py
@time: 2020/2/2 9:01
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

# def get_formatted_name(first_name,last_name):
#     '''返回整洁的姓名'''
#     full_name=first_name+' '+last_name
#     return full_name.title()
#
# musician=get_formatted_name('jimi','hendrix')
# print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

musician =get_formatted_name('jimi','hendrix')
print(musician)

musician=get_formatted_name('john','hooker','lee')
print(musician)