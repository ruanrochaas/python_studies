# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 00:04:35 2018

@author: ruan_
"""

x1,y1 = input().split()
x2,y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
distancia = ((x2-x1)**2 +(y2-y1)**2)**(1/2)
print("%.4f"%distancia)