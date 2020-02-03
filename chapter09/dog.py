# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: dog.py
@time: 2020/2/2 10:09
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

class Dog():
    '''一次模拟小狗的简单尝试'''

    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name=name
        self.age=age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+' is now sitting.')

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title()+' rolled over!')
my_dog=Dog('willie',6)

print('My dog\'s name is '+my_dog.name.title()+'.')
print('My dog is '+str(my_dog.age) + 'year old.')