#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:28:40 2020

@author: phil
"""

from Calcul_Matriciel_Fonction_2019_2020 import SaisieEntier

def Erastothene(n) :
    """
    Fonction permettant de calculer les nombres premiers inférieurs à n

    Parameters
    ----------
    n : Integer
        Valeur maximale

    Returns
    -------
    L : List
        Liste des nombres premiers inférieurs à n

    """
    L = list(range(2,n+1))
    index_p = 0
    p = L[index_p]
    test = True
    while test:
        for el in L :
            if el%p==0 and el!=p :
               L.remove(el)
        test = p**2<n
        index_p = index_p + 1
        p = L[index_p]
    return L

def Erastothene2(n) :
    """
    Fonction permettant de calculer les nombres premiers inférieurs à n
    Utilisation de filter 

    Parameters
    ----------
    n : Integer
        Valeur maximale

    Returns
    -------
    L : List
        Liste des nombres premiers inférieurs à n

    """
    L = list(range(2,n+1))
    index_p = 0
    p = L[index_p]
    test = True
    while test:
        Ltoremove = list(filter(lambda x:x%p==0,L))[1:]
        # print("Elements à supprimer ",Ltoremove)
        for el in Ltoremove :
            L.pop(L.index(el))
        test = p**2<n
        index_p = index_p + 1
        p = L[index_p]
    return L


if __name__ == "__main__" :
    n = SaisieEntier("Donnez un nombre entier supérieur à 2 : ")
    L = Erastothene(n)
    print(" Voici la liste des nombres premiers inférieurs à ",n)
    print(L)
    print("Version 2")
    L2 = Erastothene2(n)
    print(" Voici la liste des nombres premiers inférieurs à ",n)
    print(L2)
    
    
    