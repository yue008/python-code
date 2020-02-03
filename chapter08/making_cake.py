# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: making_cake.py
@time: 2020/2/2 10:01
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

##直接引用import
# import cake
#
# cake.make_cake(16,'pepperoni')
# cake.make_cake(12,'mushroom','green peppers','extra cheese')

##使用AS
# from cake import make_cake as mc
#
# mc(16,'pepperoni')
# mc(12,'mushroom','green peppers','extra cheese')

#
from cake import *

make_cake(16,'pepperoni')
make_cake(12,'mushroom','green peppers','extra cheese')


