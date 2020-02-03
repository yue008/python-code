# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: bicycles.py
@time: 2020/2/1 12:58
@contact:python初学者(微信公众号)
--------------------- 
'''
import sys
print("python版本:\n"+sys.version)
print("--------------------------\n")

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)#打印列表全部元素
print(bicycles[0])#打印列表的第一个元素
print(bicycles[0].title())#打印列表第一个元素，并首字母大写
print(bicycles[1])#打印列表的第二个
print(bicycles[3])#打印列表的第四个
print(bicycles[-1])#打印列表最后一个元素

#使用列表中的各个值，并创建一个信息
message='My first bicycle was a '+bicycles[0].title()+'.'
print(message)
