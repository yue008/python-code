# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: exercise4-5.py
@time: 2020/2/1 13:59
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys
import time

print("python版本:\n" + sys.version)
print("--------------------------\n")


start_time=time.perf_counter()
result=0
if min(range(1,1000001))==1 and max(range(1,1000001))==1000000:
    result=sum(range(1,1000001))
print(result)
print(time.perf_counter()-start_time)