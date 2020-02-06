# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: country_codes.py
@time: 2020/2/6 13:50
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    '''根据指定的国家，返回Pygal使用的两个字母的国别码'''
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    #如果没有找到指定的国家，就返回None
