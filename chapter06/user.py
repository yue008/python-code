# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: user.py
@time: 2020/2/1 17:32
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
#遍历字典中的所有键和值
for key,value in user_0.items():
    print('\nKey: '+key)
    print('\nValue: '+value)

for name,language in user_0.items():
    print(name.title()+'\'s favorite language is '+language.title()+'.')

#按照顺序遍历字典中所有键
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',}

for name in sorted(favorite_languages.keys()):
    print(name.title()+',thank you for taking the poil.')

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

#通过集合将字典中重复的值取掉
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())