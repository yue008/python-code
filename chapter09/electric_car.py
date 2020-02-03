# -*- coding: utf-8 -*-
'''
@author: acer4560g
@file: electric_car.py
@time: 2020/2/2 16:12
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
        self.make=make
        self.model=model
        self.year=year
        self.odometer_readding=0
        self.gas=100

    def get_descriptive_name(self):
        long_name=str(self.year) +' '+ self.make+' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has '+ str(self.odometer_readding) +' miles omn it')

    def update_odometer(self,mileage):
        if mileage>=self.odometer_readding:
            self.odometer_readding=mileage
        else:
            print('YOu can\'t roll back on odometer!')

    def increment_odometer(self,miles):
        self.odometer_readding+=miles

    def fill_gas_tank(self):
        print('The car\s gas tank is '+ str(self.gas)+'.')

class Battery():
    '''一次模拟电动汽车电瓶的简单尝试'''

    def __init__(self,battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size =battery_size
    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print('This car has a '+ str(self.battery_size)+'-KWh battery.')

    def get_range(self):
        '''打印一条消息，指出电瓶的续航历程'''
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go approximately "+ str(range)
        message+=' miles on a full charge'
        print(message)

class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self,make,model,year):
        '''初始化父类属性'''
        super().__init__(make,model,year)
        self.battery=Battery()
    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print('This car has a '+ str(self.battery.battery_size)+'-KWh battery.')
    def fill_gas_tank(self):
        print('Electric car doesn\'t nedd a gas tank ')

my_tesla=ElectricCar('tesla','model s',2010)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()