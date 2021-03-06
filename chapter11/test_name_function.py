# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: test_name_function.py
@time: 2020/2/3 11:35
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够正确地处理像janis Joplin这样的姓名吗？'''
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
# unittest.main()