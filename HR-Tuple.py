# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:32:05 2020

@author: vinayt
"""
readme="https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen"

t=[]
elt=int(input())
    
for j in input().split(" "):
    t.append(int(j))

t=tuple(t)

print(hash(t))        
