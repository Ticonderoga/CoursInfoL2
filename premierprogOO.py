#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:10:21 2020

@author: phil
"""


class Point():
    """
    Point en géométrie
    """
    def __init__(self,x=0,y=0,name = "O") :
        self.x = x
        self.y = y
        self.name = name

class Rectangle():
    """
    Rectangle en géométrie
    """
    def __init__(self, origine=Point(), largeur=1, hauteur=2):
        self.origine = origine
        self.largeur = largeur
        self.hauteur = hauteur
    
    def perimetre(self) :
        """
        méthode renvoyant le périmètre du rectangle

        Returns
        -------
        p : float
            valeur du perimètre

        """
        p = 2 * (self.hauteur + self.largeur)
        return p
    
    def centre(self) :
        """
        méthode renvoyant le centre du rectangle

        Returns
        -------
        C : Point
        """
        xcentre = self.origine.x + self.largeur/2
        ycentre = self.origine.y + self.hauteur/2
        C = Point(xcentre,ycentre,"centre du rectangle")
        return C

    def contient(self, P = Point()):
        testx = ((P.x) <= (self.origine.x+self.largeur)) and ((P.x)>=self.origine.x) 
        testy = ((P.y) <= (self.origine.y+self.hauteur)) and ((P.y)>=self.origine.y) 
        if testx and testy :
            return True
        else :
            return False

class Carre(Rectangle) :
    
    def __init__(self, origine = Point(), cote = 1):
        Rectangle.__init__(self, origine, largeur=cote , hauteur=cote )
        self.cote = cote

if __name__=='__main__' :
    monpoint = Point(1,2.5,"P")
    origine = Point(0,0,"O")
    maboite = Rectangle()
    maboite2 = Rectangle(monpoint, 4, 5)
    maboite3 = Rectangle(Point(5,3,"A"),12,4)
    moncarre = Carre(monpoint,2)