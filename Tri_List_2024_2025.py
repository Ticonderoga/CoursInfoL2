#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:41:28 2024

@author: phil
"""

from numpy.random import randint
from copy import deepcopy

def genList(n, high=10):
    """
    

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.
    high : TYPE, optional
        DESCRIPTION. The default is 10.

    Returns
    -------
    L : TYPE
        DESCRIPTION.

    """
    
    Tab = randint(0, high , size=n)
    L = Tab.tolist()
    return L

def permutation(x,y):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    y : TYPE
        DESCRIPTION.
    x : TYPE
        DESCRIPTION.

    """
    return y,x

def showlist(L,mesg = ''):
    """
    

    Parameters
    ----------
    L : TYPE
        DESCRIPTION.
    mesg : TYPE, optional
        DESCRIPTION. The default is ''.

    Returns
    -------
    None.

    """
    nmesg = len(mesg)
    Lstr = str(L)
    Lstr = Lstr.replace(' ','')
    nLstr = len(Lstr)
    long_affich = max(nLstr,nmesg)+6
    print("-"*long_affich)
    
    blanc_av_mess=" "*((long_affich-nmesg)//2)
    print(blanc_av_mess+mesg)
    
    blanc_av_list=" "*((long_affich-nLstr)//2)
    print(blanc_av_list+Lstr)
    
    print("-"*long_affich)

def trilist(L):
    """
    

    Parameters
    ----------
    L : TYPE
        DESCRIPTION.

    Returns
    -------
    Lout : TYPE
        DESCRIPTION.

    """
    Lout = deepcopy(L)
    permut = True
    while permut :
        permut = False
        for i in range(len(Lout)-1):
            if Lout[i]>Lout[i+1]:
                Lout[i],Lout[i+1]=permutation(Lout[i], Lout[i+1])
                permut = True
    return Lout
    
def saisientier(mesg):
    """
    

    Parameters
    ----------
    mesg : TYPE
        DESCRIPTION.

    Returns
    -------
    n : TYPE
        DESCRIPTION.

    """
    
    while True :
        try :
            n = eval(input(mesg))
            test = (type(n)!=int or (n<0))
            if not(test) :
                return n
            else :
                print("entrez un entier SVP")
        except NameError:
            print("entrez un entier SVP")

if __name__ == "__main__":
    n = saisientier('Donnez la longueur de la liste : ')
    Lnt = genList(n, high = 17)
    Lt = trilist(Lnt)
    
    showlist(Lnt,'Voici la liste non triée')
    showlist(Lt,'Voici la liste triée')
    
    