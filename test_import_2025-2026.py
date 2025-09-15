#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:39:35 2025

@author: phil
"""

from MinMaxMoy_2025_2026 import minmaxmoy

def showfiche(nom,prenom,age,email) :
    """
    Fonction permettant d'afficher un contact
    
    La sortie est de la forme suivante :
        
    Nom : Dupont
    
    Prénom : Jean
    
    Age : 55
    
    Email :jean.dupont@umlp.fr

    Parameters
    ----------
    nom : str
        Nom affiché.
    prenom : str
        Prénom affiché.
    age : int ou float
        Age.
    email : str 
        Adresse email.

    Returns
    -------
    None.

    """
    ligne = 10*'=='
    print(ligne)
    print("Nom : ", nom)
    print("Prénom : ", prenom)
    print("Age : ", age)
    print("Email : ", email)
    print(ligne)
    
def showfiche2(nom,prenom,age=6,email='toto@email.com') :
    """
    Fonction permettant d'afficher un contact
    
    La sortie est de la forme suivante :
        
    Nom : Dupont
    
    Prénom : Jean
    
    Age : 55
    
    Email :jean.dupont@umlp.fr

    Parameters
    ----------
    nom : str
        Nom affiché.
    prenom : str
        Prénom affiché.
    age : int ou float (opt.)
        Age avec une valeur par défaut à 6 ans.
    email : str (opt)
        Adresse email avec une valeur par défaut 'toto@email.com'.

    Returns
    -------
    None.

    """
    ligne = 10*'=='
    print(ligne)
    print("Nom : ", nom)
    print("Prénom : ", prenom)
    print("Age : ", age)
    print("email : ", email)
    print(ligne)

if __name__=="__main__" :
    
    showfiche("Baucour", "Philippe", 6, "toto@gmail.com")
    showfiche2("Baucour", "Philippe")
    
    showfiche2("Baucour", "Philippe",
               email = "philippe.baucour@univ-fcomte.fr")
    
    showfiche2("Baucour", "Philippe",
               email = "philippe.baucour@univ-fcomte.fr",
               age = 5)
    
    
    
    
    
    