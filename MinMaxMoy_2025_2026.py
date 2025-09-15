#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:49:02 2025

@author: phil
"""

def minmaxmoy(L) :
    """
    Fonction permettant d'obtenir le minimum, maximum 
    et la moyenne d'une liste de valeurs 

    Parameters
    ----------
    L : list
        Liste de nombres c.a.d. entiers et/ou flottants et/ou booléens 

    Returns
    -------
    m : float ou int
        minimum de L.
    M : float ou int
        maximum de L.
    moy : float ou int 
        moyenne de L.

    """
    m = min(L)
    M = max(L)
    moy = sum(L) / len(L)
    return m,M,moy

if __name__=="__main__" :
    L = [1,3,-6,8,9,2.5]
    
    p,q,r = minmaxmoy(L)
    print("où la fonction est definie ",p,q,r)

