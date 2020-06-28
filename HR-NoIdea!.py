# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 09:34:13 2020

@author: vinayt
"""
readme="https://www.hackerrank.com/challenges/no-idea/problem?h_r=next-challenge&h_v=zen"


inp=[x.strip() for x in input().split(" ")]
n=inp[0]
m=inp[1]

arr=[x.strip() for x in input().split(" ")]
a=set([x.strip() for x in input().split(" ")])
b=set([x.strip() for x in input().split(" ")])

h=0
t1= [h+1 for i in arr for j in a if i == j]
t2= [h-1 for i in arr for k in b if i == k]

print(sum(t1+t2))
