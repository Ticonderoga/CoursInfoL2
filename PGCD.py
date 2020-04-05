#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:07:38 2020

@author: phil
"""

from Calcul_Matriciel_Fonction_2019_2020 import SaisieEntier

def PGCD1(a,b):
    """
    Calcul du PGCD : Version non récursive de Hugo Philippe

    Parameters
    ----------
    a : Integer
    b : Integer

    """
    Test= True
    while Test:
        r = a % b
        if  r== 0 :
            # print("le PGCD est ", b)
            Test= False 
        elif type (b) != int:
            # print("le PGCD est ", b)
            Test= False            
        else :
            a=b
            b=r
            Test=True 
    return b


def PGCD2(a,b) :
    """
    Calcul du PGCD par récursion

    Parameters
    ----------
    a : Integer
    b : Integer

    Returns
    -------
    Integer.

    """
    if a<b :
        a,b = b,a
    r = a % b
    print('a : ',a,' b : ',b)
    print('reste : ',r)
    if r==0 :
        return b
    else :
        a = b
        b = r
        return PGCD2(a,b)

if __name__ == "__main__" :
    a = SaisieEntier("Donnez le nombre a : ")
    b = SaisieEntier("Donnez le nombre b : ")
    n = PGCD1(a,b)
    print("Version classique")
    print(" Le PGCD de ",a," et ",b," est : ",n)
    print(15*'=')
    print("Version récursive")
    n2 = PGCD2(a,b)
    print(" Le PGCD de ",a," et ",b," est : ",n2)
    
    