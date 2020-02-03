# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: survey.py
@time: 2020/2/3 13:46
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
# import sys
#
# print('本程序在python3.7.3编译，运行时请注意python版本')
# print('python当前版本:\n' + sys.version)
# print('--------------------------\n')

class AnonymousSurvey():
    '''收集匿名调查问卷的答案'''

    def __init__(self,question):
        '''存储一个问题，并为存储答案做准备'''
        self.question=question
        self.responses=[]

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)
    def store_response(self,new_response):
        '''存储单份调查问卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示手机到的所有答卷'''
        print('Survey results:')
        for response in self.responses:
            print('-'+response)