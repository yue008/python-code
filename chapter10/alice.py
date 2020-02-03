# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: alice.py
@time: 2020/2/2 20:57
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
#filename='alice.txt'
filename='English.txt'

try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg='Sorry,the file '+ filename +' does not exist'
    print(msg)
else:
    #计算文件大致包含多少单词
    words=contents.split()
    num_words=len(words)
    print('The file '+filename+'has about '+str(num_words) +' word.')
# with open(filename) as f_obj:
#     contents=f_obj.read()