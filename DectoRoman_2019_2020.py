#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:04:01 2020

@author: phil
"""


def DectoRoman(deci) :
    """
    Fonction permettant de transformer un nombre en chiffre romain

    Parameters
    ----------
    deci : Integer
        Nombre à convertir en chiffres romains.

    Returns
    -------
    rom : String
        Les chiffres romains correspondant à deci.

    """
    L_Dec = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    L_Rom = ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
    rom = ''
    test = True
    while test :
        inprocess = True
        for d,r in zip(L_Dec,L_Rom):
            if deci >= d and inprocess :
                deci = deci - d
                rom = rom + r
                inprocess = False
        test = (deci>0)
    return rom


if __name__ == "__main__" :
    nombre = 1924
    nombre_Romain = DectoRoman(nombre)
    print(nombre_Romain)





















