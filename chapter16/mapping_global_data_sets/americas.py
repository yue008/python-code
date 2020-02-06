# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: americas.py
@time: 2020/2/6 14:00
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import pygal_maps_world.maps

wm=pygal_maps_world.maps.World()
wm.title='North,Central,and Soouth America'

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','qt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
wm.render_to_file('america.svg')
