# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:31:48 2018

@author: ruan_
"""

cod1,qtd1,val1 = input().split()
cod2,qtd2,val2 = input().split()
cod1 = int(cod1)
qtd1 = int(qtd1)
val1 = float(val1)
cod2 = int(cod2)
qtd2 = int(qtd2)
val2 = float(val2)
total = qtd1*val1 + qtd2*val2
print("VALOR A PAGAR: R$ %.2f" %total)