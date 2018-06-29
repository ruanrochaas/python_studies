# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:33:49 2018

@author: ruan_
"""

A,B,C,D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B>C) and (D>A) and ((C+D)>(A+B)) and (C > 0 and D > 0) and (A % 2 == 0):
    print("Valores aceitos", end="\n")
else:
    print("Valores nao aceitos", end="\n")