# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: many_users.py
@time: 2020/2/1 18:06
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

users={
    'aeinstion':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}
for username,user_info in users.items():
    print('\nUsername:'+username)
    full_name=user_info['first']+' '+user_info['last']
    location=user_info['location']

    print('\tFull_name:' + full_name.title())
    print('\tLocation: '+location.title())