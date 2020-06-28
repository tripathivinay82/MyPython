# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:47:27 2020

@author: vinayt
"""

readme="https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"

n,m = map(int, input().split())

p1,p2="-",".|."

#Top Pattern

p1t=(m-3)//2
p2t=1

for i in range(0,n//2): 
    print((p1*p1t).rjust(0)+(p2*p2t).ljust(1)+(p2*i).ljust(i)+(p1*p1t).rjust(1))
    p1t -= 3
    p2t += 1

#Middle Pattern
p1t= (m-7)//2
p3="WELCOME"    
print((p1*p1t).rjust(0)+p3.ljust(1)+(p1*p1t).rjust(1))
    
#Bottom Pattern

p1t=3
p2t=p2t-1
j=2
for i in range(n//2, 0 , -1): 
    print((p1*p1t).rjust(0)+(p2*p2t).ljust(0)+(p2*(p2t-1)).ljust(j)+(p1*p1t).rjust(1))
    p1t += 3
    p2t -= 1
    j -= 1