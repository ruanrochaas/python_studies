# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:52:48 2018

@author: ruan_
"""

A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
maiorAB = (A + B + abs(A - B))//2
maiorABC = (maiorAB + C + abs(maiorAB - C))//2
print("%d eh o maior" %maiorABC)