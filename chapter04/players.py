# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: players.py
@time: 2020/2/1 14:44
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print("python版本:\n" + sys.version)
print("--------------------------\n")

players=['charles','martina','michael','florence','eli']
print(players[0:3])#前三个元素
print(players[1:4])#第2～4个元素
print(players[2:])#第二个元素到最后
print(players[-3:])#倒数第三个元素到最后

#遍历切片
players=['charles','martina','michael','florence','eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())