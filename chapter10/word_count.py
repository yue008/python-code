# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: word_count.py
@time: 2020/2/3 10:39
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        # msg=('Sorry,the file '+ filename+' does not exist.')
        # print(msg)
        pass
    else:
        #计算文件大致包含多少单词
        words=contents.split()
        num_words=len(words)
        print('The file '+ filename +' has about '+str(num_words) + ' words.')

filename='English.txt'
count_words(filename)

filenames=['English1.txt','English2.txt','English3.txt','English4.txt']
for file in filenames:
    count_words(file)