#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:41:28 2024

@author: phil
"""

from numpy.random import randint

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
    
       

if __name__ == "__main__":
    n = 15
    L = genList(n, high = 17)
    showlist(L,'mon message')
    