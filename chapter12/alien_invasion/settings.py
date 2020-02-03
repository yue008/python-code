# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: settings.py
@time: 2020/2/3 18:12
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
class Settings():
    '''存储《外星人入寝》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)

        #飞船的位置
        self.ship_speed_factor=1.5

        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3

