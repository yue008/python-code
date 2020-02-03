# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: alien.py
@time: 2020/2/1 15:50
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points=alien_0['points']
print('You just earned '+str(new_points)+'points!')

print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#修改字典中的值
alien_0={'color':'green'}
print('The alien is now '+alien_0['color']+'.')

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print('Original x_position: '+str(alien_0['x_position']))

#向右移动外星人
#根据外星人当前速度决定将其移动多远
if alien_0['speed']=='slow':
    x_increament=1
elif alien_0['speed']=='medium':
    x_increament=2
else:
    #这个外星人的速度一定很快
    x_increament=3
#新位置等于老位置加上增量
alien_0['x_position']=alien_0['x_position']+x_increament

print('New x_position: '+str(alien_0['x_position']))

#删除键-值对
alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

#字典嵌套
alien_0={'color':'green',
         'points':5}
alien_1={'color':'yellow',
         'points':10}
alien_2={'color':'red',
         'points':15}
aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#创建一个用于存储外星人的而空列表
aliens=[]
#创建30个绿色的外星人
for alien_number in range(30):
    new_alien={'color':'green',
               'points':5,
               'speed':'slow'}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
#显示创建了多少个外星人
print('Total number of aliens: '+str(len(aliens)))


for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15