# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: countries.py
@time: 2020/2/6 13:39
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])
