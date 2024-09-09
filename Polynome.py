#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:49:50 2024

@author: phil
"""

def poly2(x,a=1,b=1,c=1) :
    """
    Evaluation d'un polynôme d'ordre 2. La valeur de x est obligatoire 
    tandis que les valeurs des coefficients :math:`a, b, c` sont optionnels
    et par défaut égales à 1.
    
    :math:`y=ax^2+bx+c`

    Parameters
    ----------
    x : float
        abscisse.
    a : float, optional
        Coefficient d'ordre 2. The default is 1.
    b : float, optional
        Coefficient d'ordre 1. The default is 1.
    c : float, optional
        Coefficient constant. The default is 1.

    Returns
    -------
    y : float
        valeur de y calculée selon :math:`y=ax^2+bx+c`

    """
    y = a*x**2+b*x+c
    return y

def racinepoly(a=1,b=2,c=1) :
    delta = b**2 - 4*a*c
    x1 = (-b-delta**0.5)/2/a
    x2 = (-b+delta**0.5)/2/a
    return (x1,x2)

if __name__ == "__main__":
    x = 4
    y = poly2(x)
    print(x,y)
    