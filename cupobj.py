#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/11 19:18

class Cup:
    def __init__(self, height, material, capacity, color):
        self.__height = height
        self.__material = material
        self.__capacity = capacity
        self.__color = color

    def description(self):
        print(f"这个{self.__color}的杯子高{self.__height}厘米,"
              f"它是用{self.__material}做的，它可以装{self.__capacity}升的水")


cup1 = Cup(30, '玻璃', 1.5, '白色')
cup1.description()
