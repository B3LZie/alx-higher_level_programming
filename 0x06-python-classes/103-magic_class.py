#!/usr/bin/python3
""" class Square that defines a square"""


import math


class MagicClass:
    """ class Square that defines a square"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError('radius must be a number')
            self.__radius = radius

    def area(self):
        return self.__radius**2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius