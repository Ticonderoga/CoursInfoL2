#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:56:53 2020

@author: phil
"""
def IsNumericList(L):
    """
    Fonction testant une liste avec des valeurs numériques

    Parameters
    ----------
    L : List
        Liste quelconque

    Returns
    -------
    test : Boolean
        test est vrai si toutes les valeurs sont numériques
    """
    try :
        
        res = True
        i = 0
        while i<len(L) :
            if (type(L[i])!= int) and not(type(L[i])== float):
                return False
            elif (type(L[i])!= float) and not(type(L[i])== int) :
                return False
            else :
                i=i+1
        return res
        
    except IndexError :
        print("Vous devez avoir une liste non vide")
    

def MinMaxMoy(L) :
    """
    Fonction permettant de calculer le minimum, le maximum et la moyenne

    Parameters
    ----------
    L : List
        Liste avec des données numériques

    Returns
    -------
    T : Tuple
        Tuple (Min,Max,Moy)

    """
    try :
        if IsNumericList(L) :
            mini = L[0]
            maxi = L[0]
            S = L[0]
            for e in L[1:] :
                S = S + e
                if e > maxi :
                    maxi = e
                if e < mini :
                    mini = e
     
            moy = S / len(L)
            return mini,maxi,moy
        else :
            print("Vous devez avoir une liste avec des nombres")
    except IndexError :
        print("Vous devez avoir une liste non vide")
    
    

if __name__ == '__main__' :
    L = [3,4,6,8,11,-1,67]
    m,M,mo = MinMaxMoy(L)
    
    
    
    
    
    
    