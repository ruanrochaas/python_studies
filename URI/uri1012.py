# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:43:12 2018

@author: ruan_
"""

A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
areaTri = A*C/2
areaC = 3.14159*C**2
areaTrap = (A+B)*C/2
areaQ = B*B
areaR = A*B
print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(areaTri,areaC,areaTrap,areaQ,areaR))