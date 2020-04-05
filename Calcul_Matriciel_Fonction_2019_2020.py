#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 08:22:23 2020
Programme fonctionnel pour la multiplicationn matricielle
@author: Philippe Baucour

"""

def SaisieEntier(message) :
    """
    Fonction permettant de saisir un entier avec
    un message spécifique :

    Parameters
    ----------
    message : String
        Message à afficher pour poser la question

    Returns
    -------
    n : Integer
        Valeur retournée avec n > 0

    Example
    -------
    >>> mesg = "Donnez un entier : "
    >>> n = SaisieEntier(mesg)
    Donnez un entier : -1
    Donnez un entier : 2.3
    Donnez un entier : djklqsdjslk
    Donnez un entier : 4
    >>> print(n)
    4
    """
    test=True
    while test :
            try :
                n=eval(input(message))
                test = type(n)!= int or n<=0
            except NameError :
                print("Veuillez entrer un nombre entier positif")
                # message = message +' [SVP] '
    return n

def TestTaille(taille1,taille2):
    """
    Fonctionnant permettant de tester 2 tailles de matrices pour effectuer une
    multiplication matricielle ?
    Les tailles sont des tuples de 2 entiers i.e. (m,n)

    Parameters
    ----------
    taille1 : Tuple
        Taille de la matrice M1. (m,n) avec
        m nbre de lig de M1
        n nbre de col de M1

    taille2 : Tuple
        Taille de la matrice M2. (p,q) avec
        p nbre de lig de M2
        q nbre de col de M2

    Returns
    -------
    res : Boolean
        Résultat du test.

    Example
    -------
    >>> res = TestTaille((3,4),(4,5))
    >>> print(res)
    True
    >>> res = TestTaille((3,4),(5,4))
    >>> print(res)
    False

    """
    res = False
    if taille1[1]==taille2[0] :
        res = True
    return res


def SaisieTaille(nomMat):
    """
    Saisie d'une taille de matrice

    Parameters
    ----------
    nomMat : string
        nom de la matrice

    Returns
    -------
    T : tuple
        un tuple (m,n) avec m le nb de lig et n le nb de col

    Example
    -------
    >>> taille = SaisieTaille("A")
    Veuillez entrer la taille de la matrice A
    Donnez le nombre de lignes : 4
    Donnez le nombre de colonnes : 5
    >>> print(taille)
    (4,5)
    """
    print("Veuillez entrer la taille de la matrice "+nomMat)
    m = SaisieEntier("Donnez le nombre de lignes : ")
    n = SaisieEntier("Donnez le nombre de colonnes : ")

    return (m,n)

def SaisieMatrice(nomMat,taille) :
    """
    Fonction permettant de saisir une matrice de taille donnée

    Parameters
    ----------
    nomMat : String
        Nom de la matrice utilisée pour poser les différentes questions
    taille : Tuple
        Taille de la matrice (m,n) avec\n
        m : nb de lignes\n
        n : nb de colonnes\n

    Returns
    -------
    M : List
        une liste de listes avec chaque sous-liste représentant une ligne

    Example
    -------
    >>> M = SaisieMatrice("M",(2,2))
    M[1,1] = 1
    M[1,2] = 2
    M[2,1] = 3
    M[2,2] = 4
    >>> print(M)
    [[1, 2], [3, 4]]
    """

    la,ca = taille
    A = [[None]*(ca) for i in range(la)]
    for i in range(la):
        for j in range(ca):
            QuestA = nomMat+"["+str(i+1)+","+str(j+1)+"] = "
            A[i][j] = eval(input(QuestA))

    return A

def AfficheMatrice(nomMat,M) :
    """
    Fonction permettant d'afficher à une matrice avec un nom

    Parameters
    ----------
    nomMat : String
        Nom de la matrice.
    M : Liste
        Matrice sous forme d'une liste de listes.

    Returns
    -------
    >>> M = [[1, 2], [3, 4]]
    >>> AfficheMatrice("M",M)
      _________
     /Matrice M\_______________
     M =
      1      2
      3      4
    """
    # Affichage de M
    print(" _________")
    print("/Matrice "+nomMat+"\_______________")
    print(nomMat+" = ")
    lM = len(M)
    cM = len(M[0])
    for i in range(lM):
        for j in range(cM):
            print("     ", M[i][j], end="")
        print("")

def MultiplicationMatrice(A,B) :
    """
    Fonction permettant de multiplier deux matrices

    Parameters
    ----------
    A : List
        Matrice A au format liste de listes
    B : List
        Matrice B au format liste de listes

    Returns
    -------
    C : List
        Matrice C au format liste de listes

    Example
    -------
    >>> A = [[1, 2], [3, 4]]
    >>> B = [[0, 1], [1, 0]]
    >>> C = MultiplicationMatrice(A,B)
    >>> print(C)
    [[2.0, 1.0], [4.0, 3.0]]

    On peut aussi afficher la matrice via AfficheMatrice

    >>> AfficheMatrice("C",C)
      _________
     /Matrice C\_______________
     C =
      2      1
      4      3
    """
    tailleA = (len(A),len(A[0]))
    tailleB = (len(B),len(B[0]))

    if not(TestTaille(tailleA, tailleB)) :
        print("Tailles de matrices incompatibles")
        print("Impossibilité de multiplier ")
        print(str(tailleA)+" X "+str(tailleB))
    else :
        lc, cc = tailleA[0], tailleB[1]
        C = [[None]*(cc) for i in range(lc)]
        for i in range(lc):
            for j in range(cc):
                S = 0.
                for k in range(len(A[0])):
                    S = S + A[i][k]*B[k][j]
                C[i][j] = S

        return C


if __name__ == '__main__' :
    test = True
    while test :
        tailleA = SaisieTaille("A")
        tailleB = SaisieTaille("B")
        test = not(TestTaille(tailleA,tailleB))

    A = SaisieMatrice("A",tailleA)
    AfficheMatrice("A",A)
    B = SaisieMatrice("B",tailleB)
    AfficheMatrice("B",B)
    C = MultiplicationMatrice(A,B)
    AfficheMatrice("C",C)
