# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:37:14 2020

@author: vinayt
"""

readme="https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen"
#s=str(input())
s="qA2"
an=0
ab=0
d=0
l=0
u=0
for i in range(len(s)):
    if s[i].isalnum():
        an=1 
    if s[i].isalpha():
        ab = 1 
    if s[i].isdigit():
        d = 1
    if s[i].islower():
        l = 1
    if s[i].isupper():
        u = 1
    
print("True") if an == 1 else print("False")
print("True") if ab == 1 else print("False")
print("True") if d == 1 else print("False")
print("True") if l == 1 else print("False")
print("True") if u == 1 else print("False")

