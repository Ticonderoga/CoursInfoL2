#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:06:50 2020

@author: phil
"""


class Vector(object):
    """
    Documentation de vecteur
    """
    def __init__(self,u=0,v=0):
        self.__x = u
        self.__y = v

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def setx(self,u):
        self.__x = u

    def sety(self,v):
        self.__y = v
    
    def __str__(self):
        return "(%.3f,%.3f)" % (self.__x,self.__y)

    def __repr__(self):
        return "Vector(%.3f,%.3f)" % (self.__x,self.__y)

    def __add__(self, other):
        if isinstance(other, Vector):
            newx = self.__x + other.__x
            newy = self.__y + other.__y
            return Vector(newx, newy)
        
    def __truediv__(self, other):
        if isinstance(other, Vector):
            newx = self.__x / other.__x
            newy = self.__y / other.__y
            return Vector(newx, newy)

    def __mul__(self, constant):
        if type(constant)==float or type(constant)==int:
            newx = self.__x * constant
            newy = self.__y * constant
            return Vector(newx, newy)

    def __eq__(self,other):
        if isinstance(other, Vector):
            testx = self.__x == other.__x
            testy = self.__y == other.__y
            return testx and testy

    def norm(self):
        x2 = self.__x**2
        y2 = self.__y**2
        return (x2+ y2)**(1/2)

class Multiplier(object):
    def __init__(self,constant):
        self.constant = constant

    def __call__(self,other):
        return self.constant*other

if __name__=='__main__' :    
    v1 = Vector(3, 4)
    print(v1)
    v2 = Vector(12,-2)
    print(v2)