# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: languages_survey.py
@time: 2020/2/3 13:57
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

from survey import AnonymousSurvey



#定义一个问题，并创建一个表示调查的AnonymusSurvey对象
question='What language did you first learn to speak?'
my_survey=AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print('Enter \'q\' at any time to quit.\n')
while True:
    response=input('language：')
    if response=='q':
        break
    my_survey.store_response(response)

#显示调查结果
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()