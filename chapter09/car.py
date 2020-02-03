# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: car.py
@time: 2020/2/2 15:50
@contact:python初学者(微信公众号)
@vision:3.7.3 
--------------------- 
'''
import sys

print('本程序在python3.7.3编译，运行时请注意python版本')
print('python当前版本:\n' + sys.version)
print('--------------------------\n')

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        '''返回整洁嗯描述性信息'''
        long_name=str(self.year) + ' '+ self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车历程的信息'''
        print('This car has '+str(self.odometer_reading) +' miles on it')

    def update_odometer(self,mileage):
        '''
        将里程表设置为指定的值
        禁止将历程表读数往回调
        :param mileage:
        :return:
        '''
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self,miles):
        self.odometer_reading+=miles
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
