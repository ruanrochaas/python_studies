# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 00:43:36 2018

@author: ruan_
"""

N = int(input("Digite: "))
horas = int(N / 3600)
minutos = int(N % 3600 / 60)
segundos = int(N % 60)
print("%d:%d:%d" %(horas,minutos,segundos))