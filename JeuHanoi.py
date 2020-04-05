#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:08:09 2020

@author: phil
"""

from Calcul_Matriciel_Fonction_2019_2020 import SaisieEntier

def hanoi (n,de,a,par) :
    """
    Fonction simulant le jeu des Tours de Hanoï

    Parameters
    ----------
    n : Integer
        Nombre de disques
    de : Integer
        Tour de départ
    a : Integer
        Tour d'arrivée.
    par : Integer
        Tour intermédiaire
    """
    
    if n > 0 :
        # print("hanoi(",n-1,",",de,",",par,",",a,")")
        hanoi(n-1,de,par,a)
        print("Tour : ",str(de),"−> Tour : ",str(a))
        # print("hanoi(",n-1,",",par,",",a,",",de,")")
        hanoi(n-1,par,a,de)
        
if __name__ == "__main__" :
        n = SaisieEntier("Donnez le nombre de disques : ")
        hanoi(n,1,3,2)
        
        
        
        
        
        
        
        
        
        
        
    