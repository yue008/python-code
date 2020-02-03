# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: confirmed_users.py
@time: 2020/2/2 8:38
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
#首先，创建一个待验证用户列表
#和一个用于存储已验证用户的空列表

unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的列表都已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print('Verifying user '+ current_user.title())
    confirmed_users.append(current_user)

#显示所有已验证的用户
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
