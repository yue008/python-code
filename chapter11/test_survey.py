# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: test_survey.py
@time: 2020/2/3 14:13
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''

#     def test_store_single_response(self):
#         '''测试单个答案会被妥善地存储'''
#         question='What language did you first learn to speak?'
#         my_survey=AnonymousSurvey(question)
#         my_survey.store_response('English')
#
#         self.assertIn('English',my_survey.responses)
#     def test_store_three_responses(self):
#         '''测试三个答案会被妥善存储'''
#         question='What language did you first learn to speak?'
#         my_survey=AnonymousSurvey(question)
#         responses=['English','Spanish','Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
#
# # unittest.main()
    def setUp(self):
        '''创建一个调查对象和一组答案，工使用的测试方法使用'''
        question='What language did you first learn to speak?'
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']

    def test_store_single_response(self):
        '''测试单个答案会被妥善地存储'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        '''测试三个答案会被妥善地存储'''
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

