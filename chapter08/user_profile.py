# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: user_profile.py
@time: 2020/2/2 9:44
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def build_profile(first,last,**user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

user_profile=build_profile('albert','einstein',
                           location='princeton',field='physics')

print(user_profile)
