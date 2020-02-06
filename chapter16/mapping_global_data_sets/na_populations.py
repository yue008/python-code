# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: na_populations.py
@time: 2020/2/6 14:10
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import pygal_maps_world.maps

wm=pygal_maps_world.maps.World()
wm.title='Population of Countries in North America'
wm.add('North America',{'ca':34126000,'us':309349000,'mx':113423000})

wm.render_to_file('na_population.svg')