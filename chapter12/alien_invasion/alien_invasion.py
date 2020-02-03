# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: alien_invasion.py
@time: 2020/2/3 18:01
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()