# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: magicians.py
@time: 2020/2/1 13:39
@contact:python初学者(微信公众号)
--------------------- 
'''

import sys
print("python版本:\n"+sys.version)
print("--------------------------\n")

#遍历整个列表
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
#更多操作
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+',that was a great trick!')
    print('I can\'t wait to see your next trick,'+magician.title()+'.\n')
print('Thank you everyone,That was a great magic show!')