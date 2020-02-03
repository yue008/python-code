# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: mountain.py
@time: 2020/2/2 8:46
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

responses={}

#设置一个标志，指出调查是否继续
polling_active=True

while polling_active:
    #提示输入被调查者的名字和回答
    name=input('\nWhat is yur name?')
    response=input('Which mountain would youo like to climb someday?')

    #将答案存储在字典中
    responses[name]=response

    #看看是否还有人要参与调查
    repeat=input('Would you like to let another person respond?(yes / no)')
    if repeat=='no':
        polling_active=False

#调查结束，显示结果
print('\n--- Poll Results ---')
for name,response in responses.items():
    print(name+' would like to climb '+ response +'.')