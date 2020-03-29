#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:00:18 2020

@author: phil
"""


def factorielle(n):
    if n==1 :
        return 1
    else :
        return n*factorielle(n-1)

if __name__ == "__main__":
    print(factorielle(10))