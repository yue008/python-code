# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: remember_me.py
@time: 2020/2/3 11:03
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
import json

# username=input('What is your name?')
#
# filename='username.json'
# with open(filename,'w') as f_obj:
#     json.dump(username,f_obj)
#     print('We\'ll remember you when you come back,'+username+'!')

# def greet_user():
#     '''问候用户，并指出其姓名'''
#     #如果以前存储了用户名，就加载它
#     #否则，就表示用户输入用户名并存储它
#     filename='username.json'
#     try:
#         with open(filename)as f_obj:
#             username=json.load(f_obj)
#     except FileNotFoundError:
#         username=input('What is your name?')
#         with open(filename,'w') as f_obj:
#             json.dump(username,f_obj)
#             print('We\'ll remember you when you come back,'+username+'!')
#     else:
#         print('Welcome back,'+username+'!')
# greet_user()

def get_stored_username():
    '''如果存储了用户名，就获取它'''
    filename='username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    '''问候用户，并指出其姓名'''
    username=get_stored_username()
    if username:
        print('Welcome back,'+username+'!')
    else:
        username=input('What is your name?')
        filename='username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print('We\'ll remember youo when you come back,'+ username+'!')
greet_user()