#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:59:37 2020
@author: Philippe Baucour
"""

class Atome:
    """atomes simplifiés, choisis parmi les 10 premiers éléments du TP"""
    __table__ =[None, ('hydrogène',0), ('hélium',2), ('lithium',4),
    ('béryllium',5), ('bore',6), ('carbone',6), ('azote',7),
    ('oxygène',8), ('fluor',10), ('néon',10)]
    def __init__(self, nat):
        "le n. atomique détermine le n. de protons, d'électrons et de neutrons"
        self.np, self.ne = nat, nat
        # nat = numéro atomique
        self.nn = Atome.__table__[nat][1]
        # nb. de neutrons trouvés dans table
        self.nom = Atome.__table__[nat][0]
    def affiche(self):
        print()
        print("Nom de l'élément :", self.nom)
        print("%s protons, %s électrons, %s neutrons" % \
        (self.np, self.ne, self.nn))

#%%
class Ion(Atome):
    """les ions sont des atomes qui ont gagné ou perdu des électrons"""
    def __init__(self, nat, charge):
        "le n. atomique et la charge électrique déterminent l'ion"
        Atome.__init__(self, nat)
        self.ne = self.ne - charge
        self.charge = charge
    def affiche(self):
        "cette méthode remplace celle héritée de la classe parente"
        Atome.affiche(self)
        # ... on utilise Atome.affiche !
        print("Particule électrisée. Charge =", self.charge)

#%%
### Programme principal : ###
if __name__ == "__main__" :
    XXfgf = Atome(5)
    Li_p = Ion(3, 1)
    O_2m = Ion(8, -2)
    # B.affiche()
    Li_p.affiche()
    O_2m.affiche()
