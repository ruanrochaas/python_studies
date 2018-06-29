# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 02:22:48 2018

@author: ruan_
"""

lista = [[1,"Cachorro Quente",4.00],[2,"X-Salada",4.50],[3,"X-Bacon",5.00],[4,"Torrada Simples",2.00],[5,"Refrigerante",1.5]]
cod,numP = input().split()
cod = int(cod)
numP = int(numP)
valor = lista[cod - 1][2]*numP

print("Total: R$ %.2f" %valor)