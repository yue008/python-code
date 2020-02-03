# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: favorite_languages.py
@time: 2020/2/1 17:28
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',}
print('Sarah\'s favorite alnguage is '+ favorite_languages['sarah'].title()+'.')


#字典多值
favorite_languages={
    'jen':['python','ruby'],
    'sarah':'c',
    'edward':['go','ruby'],
    'phil':['python','haskbell']}
for name,languages in favorite_languages.items():
    print('\n'+name.title()+'\'s favorite languages are:')
    for language in languages:
        print('\t'+language.title())
