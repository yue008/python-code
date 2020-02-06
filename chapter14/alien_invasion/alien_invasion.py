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
from alien import Alien
import game_function as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')


    #创建Play按钮
    play_button=Button(ai_settings,screen,'Play')
    #创建一个用于存储游戏统计信息嗯实例
    stats=GameStats(ai_settings)
    #创建飞船
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人
    aliens=Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建存储游戏统计信息的实例，并创建记分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)

        gf.update_screen(ai_settings,screen,ship,sb,aliens,bullets,stats,play_button)



run_game()