# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:13:25 2018

@author: ruan_
"""

valor = float(input())

notas100 = int(valor//100)
notas50 = int(valor%100//50)
notas20 = int(valor%100%50//20)
notas10 = int(valor%100%50%20//10)
notas5 = int(valor%100%50%20%10//5)
notas2 = int(valor%100%50%20%10%5//2)

moeda100 = int(valor%100%50%20%10%5%2//1)
moeda50 = int(valor%100%50%20%10%5%2%1*100//50)
moeda25 = int(valor%100%50%20%10%5%2%1*100%50//25)
moeda10 = int(valor%100%50%20%10%5%2%1*100%50%25//10)
moeda5 = int(valor%100%50%20%10%5%2%1*100%50%25%10//5)
moeda1 = int(valor%100%50%20%10%5%2%1*100%50%25%10%5//1)

print('''NOTAS:
%d nota(s) de R$ 100.00
%d nota(s) de R$ 50.00
%d nota(s) de R$ 20.00
%d nota(s) de R$ 10.00
%d nota(s) de R$ 5.00
%d nota(s) de R$ 2.00
MOEDAS:
%d moeda(s) de R$ 1.00
%d moeda(s) de R$ 0.50
%d moeda(s) de R$ 0.25
%d moeda(s) de R$ 0.10
%d moeda(s) de R$ 0.05
%d moeda(s) de R$ 0.01''' %(notas100,notas50,notas20,notas10,notas5,notas2,moeda100,moeda50,moeda25,moeda10,moeda5,moeda1))