# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: my_car.py
@time: 2020/2/2 16:45
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

# from electric_car import Car
#
# my_new_car =Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
#
# from electric_car import ElectricCar
# my_tesla=ElectricCar('tesla','model s',2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

from electric_car import Car,ElectricCar
my_beetle=Car('volkswageen','beetle',2016)
print(my_beetle.get_descriptive_name())

My_tesla=ElectricCar('tesla','roadster',2016)
print(My_tesla.get_descriptive_name())