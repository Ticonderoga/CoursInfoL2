#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 08:28:30 2024

@author: phil
"""
class Vector():
    "Définition d'un vecteur"
    def __init__(self,x=0,y=0,name='V') :
        self.x = x
        self.y = y 
        self.name = name
        
    def norm(self):
        return (self.x**2+ self.y**2)**0.5
    

class Point():
    "Définition d'un point mathématique"
    
    def __init__(self,x=0,y=0,name='O') :
        self.x = x
        self.y = y 
        self.name = name
    
    def move(self,vect=Vector(0,0)) :
        self.x = self.x + vect.x
        self.y = self.x + vect.y
        

class Rectangle() :
    "Définition d'un rectangle"
    def __init__(self,origine = Point(),largeur = 2, hauteur =1) :
        self.origine = origine
        self.largeur = largeur
        self.hauteur = hauteur
    
    def surface(self):
        """
        Calcul de la surface du rectangle

        Returns
        -------
        float
            surface du rectangle calculé à partir 
            de la hauteur et la largeur.

        """
        
        return self.largeur * self.hauteur
    
    def perimeter(self):
        return 2*(self.largeur + self.hauteur)
    
    def centre(self) :
        xcentre = self.origine.x + self.largeur/2
        ycentre = self.origine.y + self.hauteur/2
        return Point(xcentre,ycentre,"centre du rectangle")
        
    def contains(self,P=Point()) :
        testx = self.origine.x <=P.x<=(self.origine.x + self.largeur)
        testy = self.origine.y<=P.y<=(self.origine.y + self.hauteur)
        
        return testx and testy
      
class Carre(Rectangle) :
    def __init__(self,origine=Point(),cote=1):
        self.cote =cote
        self.largeur = self.cote
        self.hauteur = self.cote
        self.origine= origine
        Rectangle.__init__(self.origine,self.cote,self.cote)
    
    def scale(self,scl_factor = 2):
        self.cote = self.cote * scl_factor
        self.largeur = self.cote
        self.hauteur = self.cote
    
    def move(self,v=Vector(0,0)):
        self.origine.move(v)
        
        
        
if __name__=='__main__' :    
    monpoint = Point(1,2.5,'A')
    print("monpoint")
    print(monpoint.x)
    print(monpoint.y)
    
    rect = Rectangle(monpoint,2,5)
    rect.surface()
    rect.perimeter()
    P = Point(2,7)
    if rect.contains(P) :
        print("P est dans le rectangle")
    else :
        print("P n'est pas dans le rectangle")
    
    C = Carre(P,3)
    C.contains(Point(-2,6)) # False
    C.contains(Point(3,5))  # True
    