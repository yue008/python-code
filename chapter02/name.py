# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: name.py
@time: 2020/2/1 10:53
@contact:python初学者(微信公众号)
--------------------- 
'''


import sys
print("python版本:\n"+sys.version)
print("--------------------------\n")
#使用方法修改字符串大小写
name="ada lovelace"
print(name.title())#首字母大写
name="Ada Lovelace"
print(name.upper())#全部大写
print(name.lower())#全部小写

#合并(拼接)字符串
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name

print(full_name)

#拼接2
print("hello,"+full_name.title())

#拼接3
message="hello,"+full_name.title()
print(message)