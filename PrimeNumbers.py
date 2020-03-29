#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemples de listing,
Implémentation du crible d'Ératosthène

Ce script calcule les nombres premiers inférieurs à N 
en appliquant la méthode du crible d'Ératosthène.

calcul des nombres premiers inferieurs a N
initialisation
"""

from copy import * # permet de faire des copies de variables 

def eratosthene_V1(l):
    liste=copy(l)   # on travaille sur une copie de l afin de ne pas 
                    # modifier la liste originelle
    nombre = 2
    N=l[-1]
    while (nombre*nombre <= N):     # tant que le nb premier < a la
                                    # racine carree de N
                                    # parcourt la liste avec ce nombre
       for i in liste[ liste.index(nombre) + 1: ]: 
           if i % nombre == 0:  # un multiple du nombre est trouve
               del( liste[ liste.index(i) ] )   # on le raye de la liste
       nombre = liste[liste.index(nombre) + 1]  # on prend le nombre 
                                                # suivant non raye
    
    return liste[1:]                            #affichage du resultat



# Voici une version algorithmiquement équivalente mais beaucoup plus rapide 
# qui exploite la puissance du type liste de Python :

def eratosthene_V2(l):
    liste    = copy(l)
    #liste[1] = 0
    nombre = 2
    N=l[-1]
    while (nombre ** 2 <= N):   # tant que le nombre a examiner est inferieur a
                                # la racine carree de N
       
       #eliminer tous les multiples du nombre
       liste[ nombre*2 :: nombre ] = [0] * ((N // nombre) - 1) 

       # passer au nombre non examine suivant
       nombre = nombre+ 1
       while not liste[nombre]:
           nombre = nombre+1
    
    liste = list(filter (None, liste))
    return liste                 # et a la fin, on affiche le resultat

#Que l'on peut enfin réduire à :

def eratosthene_V3(l):
    nombre=2
    liste=copy(l)
    #liste[1] = 0
    N=l[-1]
    while nombre**2 <= N:
       liste[nombre*2 :: nombre] = [0]*len(liste[nombre*2 :: nombre])
       nombre =nombre+ 1   
    
    return list(filter(None, liste))


def eratosthene_recursif(liste):
    """ j'ai mal à la tête ..."""
    return liste and [liste[0]] + \
        eratosthene_recursif([i for i in liste if i%liste[0]])


def eratosthene_recursif2(liste):
    """ recursif plus explicite"""
    if not liste:  # not liste donne True si L est vide
        return []
    else:
        L=[]
        for i in liste:
            if i%liste[0] :
                L.append(i)
        return [liste[0]] + eratosthene_recursif2(L)



if __name__=='__main__' :
    # ============== Eratosthène ==============
    n=eval(input("Donnez le nombre n :"))
    while n<2 :
        n=eval(input("Donnez le nombre n > 2:"))
    
    liste_init=list(range(n+1))
    
    L_premier1=eratosthene_V1(liste_init)
    print("Version 1 ")
    print(L_premier1)
    L_premier2=eratosthene_V2(liste_init)
    print("Version 2 ")
    print(L_premier2)
    L_premier3=eratosthene_V3(liste_init)
    print("Version 3 ")
    print(L_premier3)
    L_premier4=[1]+eratosthene_recursif(liste_init[2:])
    print("Version 4 ")
    print(L_premier4)
    L_premier5=[1]+eratosthene_recursif2(liste_init[2:])
    print("Version 5 ")
    print(L_premier5)
    
