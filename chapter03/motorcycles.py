# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: motorcycles.py
@time: 2020/2/1 13:16
@contact:python初学者(微信公众号)
--------------------- 
'''

import sys
print("python版本:\n"+sys.version)
print("--------------------------\n")


motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

#列表中添加元素
motorcycles[0]='ducati'
print(motorcycles)


#列表中添加元素,添加元素到列表末尾
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#在列表指定位置插入元素，根据索引
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)

#列表删除元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]#利用del，通过索引删除
print(motorcycles)
#删除的另一种方法：pop的用法
#默认删除最后一个元素，变量接受删除的元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

pop_motorcycle=motorcycles.pop()
print(motorcycles)
print(pop_motorcycle)

#根据列表元素删除
#只删除第一个指定的值，如果删除的值在列表中有多个，则需要循环
motorcycles=['honda','yamaha','suzuki','yamaha']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)




