# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:05:42 2018

@author: ruan_
"""

idade = int(input())
anos = int(idade//365)
meses = int(idade%365//30)
dias = int(idade%365%30)
print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(anos, meses, dias))