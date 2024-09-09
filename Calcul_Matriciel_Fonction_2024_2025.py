#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:42:11 2024

@author: phil
"""
from numpy import linspace

def saisietaille(nomM='M'):
    """
    Fonction de saisie de la taille d'une matrice,
    on peut donner son nom en paramètre d'entrée

    Parameters
    ----------
    nomM : String Optionnel
        Nom de la matrice. Par défaut on a 'M'

    Returns
    -------
    sizeM : tuple of int
        Tupple formé du nombre de lignes et de colonne 
        de la matrice (nlig, ncol).

    Examples
    --------
    >>> saisietaille('M')
    Saisie de la taille de M
    Nombre de lignes et de colonnes (nlig,ncol): 4,3
    (4, 3)
    """
    print("Saisie de la taille de ",nomM)
    nlig, ncol = eval(input("Nombre de lignes et de colonnes (nlig,ncol): "))
    return (nlig, ncol)

def testtaille(sizeA, sizeB):
    nligA, ncolA = sizeA
    nligB, ncolB = sizeB
    test = ncolA==nligB
    return test
    
def saisieMatrice(nomM,sizeM) :
    nlig, ncol = sizeM
    M = [[None]*ncol for i in range(nlig)]
    
    for i in range(nlig):
        for j in range(ncol) :
            Quest = nomM+'('+str(i+1)+','+str(j+1)+')= '
            M[i][j] = eval(input(Quest))
    return M

def produitMatrice(matA, matB):
    nligA, ncolA = len(matA),len(matA[0])
    nligB, ncolB = len(matB),len(matB[0])
    nligP, ncolP = nligA, ncolB
    P = [[None]*ncolP for i in range(nligP)]
    for i in range(nligP) :
        for j in range(ncolP) :
            S = 0
            for k in range(ncolA) :
                S = S + matA[i][k] * matB[k][j]
            P[i][j] = S
    return P

def afficheMatrice(nomM,matM) :
    print(nomM,'=')
    nligM, ncolM = len(matM),len(matM[0])
    for i in range(nligM):
        for j in range(ncolM):
            print('    ',matM[i][j],end='')
        print("")

if __name__ =="__main__" :
    sizeA = saisietaille("A")
    sizeB = saisietaille("B")
    while not(testtaille(sizeA, sizeB)) :
        print("Tailles de matrices incompatibles")
        sizeA = saisietaille("A")    
        sizeB = saisietaille("B")
        
    A = saisieMatrice('A',sizeA)
    afficheMatrice('A', A)
    B = saisieMatrice('B',sizeB)
    afficheMatrice('B', B)
    C = produitMatrice(A, B)
    afficheMatrice("C", C)


            
    
    
    