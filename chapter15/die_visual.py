# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: die_visual.py
@time: 2020/2/5 18:02
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
from die import Die
import pygal

#创建一个D6
die=Die()

#掷几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)

#分析结果
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist=pygal.Bar()

hist.title='Result of rolling one D6 1000 times.'
hist.x_labels=['1','2','3','4','5']
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')