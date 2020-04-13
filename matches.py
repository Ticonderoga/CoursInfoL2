#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:37:20 2020

@author: phil
"""

def matchs(Joueurs) :
    """
    Fonction récursive permettant de planifier les matchs
    entre différents joueurs (1 seule confrontation à chaque fois)
    
    Parameters
    ----------
    Joueurs : List
        Liste des joueurs du type ["David","Philippe","Pierre","Henri"].

    Returns
    -------
     Liste de tuples du type [ ("David","Philippe"), ("David","Pierre"),
                              ("David","Henri"), ... ("Pierre","Henri")]

    """
    if len(Joueurs) == 1 :
        return []
    else :
        joueur0 = Joueurs[0]
        L =[]
        for j in Joueurs[1:] :
            m = (joueur0,j)
            L.append(m)
        
        return L + matchs(Joueurs[1:])


if __name__ == '__main__' :
    Joueurs = ["David","Philippe","Pierre","Henri"]
    L_matchs = matchs(Joueurs)
    for m in L_matchs :
        print(m[0],' vs ',m[1])