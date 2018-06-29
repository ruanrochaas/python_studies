# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:57:13 2018

@author: ruan_
"""

A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

delta = (B*B) - (4*A*C)

if delta <= 0 or A == 0.0:
    print("Impossivel calcular")
else:
    r1 = (-B + delta**(1/2))/(2*A)
    r2 = (-B - delta**(1/2))/(2*A)
    print("R1 = %.5f\nR2 = %.5f" %(r1,r2))