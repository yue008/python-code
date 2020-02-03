# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: favorite_languages.py
@time: 2020/2/2 17:20
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

#OrderedDicit和字典功能几乎相同，但可以记录键-值对的添加顺序
from collections import OrderedDict

favorite_language=OrderedDict()

favorite_language['jen']='python'
favorite_language['sarah']='c'
favorite_language['edward']='rudy'
favorite_language['phil']='python'

for name,language in favorite_language.items():
    print(name.title()+'\'s favorite language is '+
          language.title()+'.')


from random import randint
x=randint(1,6)
print(x)