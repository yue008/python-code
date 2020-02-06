# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: highs_lows.py
@time: 2020/2/5 20:28
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高气温和日期
filename='sitka_weather_full_2014.csv'
with open(filename,encoding='utf-8-sig') as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows=[],[],[]
    for row in reader:
        if row[2] and row[8] and row[9]:
            current_date =datetime.strptime(row[2],'%Y/%m/%d')
            dates.append(current_date)

            high=int(row[8])
            highs.append(high)

            low=int(row[9])
            lows.append(low)
#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形的格式
plt.title('Daliy high temperatures,July 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()