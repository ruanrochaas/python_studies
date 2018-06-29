# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 00:21:57 2018

@author: ruan_
"""

valor1 = int(input())

valor = valor1
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

while valor != 0:
    if valor >= 100:
        notas100 = valor//100
        valor = valor%100
    elif valor >= 50:
        notas50 = valor//50
        valor = valor%50
    elif valor >= 20:
        notas20 = valor//20
        valor = valor%20
    elif valor >= 10:
        notas10 = valor//10
        valor = valor%10
    elif valor >= 5:
        notas5 = valor//5
        valor = valor%5
    elif valor >= 2:
        notas2 = valor//2
        valor = valor%2
    elif valor >= 1:
        notas1 = valor//1
        valor = valor%1

print(valor1)
print("%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00\n" %(notas100,notas50,notas20,notas10,notas5,notas2,notas1), end="")