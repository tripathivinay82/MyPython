# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:20:07 2020

@author: vinayt
"""

var=input("Please Enter The String:")
var=var.lower()
out=''
c1=len(var)-1

while c1 >= 0:
    for a in range(len(var)):
        out=out+var[c1]
        break
    c1=c1-1

print("Reverse of entered word is:",out)
if out == var:
    print(var + " is a Palindrome Word!!!")
else:
    print(var + " is not a Palindrome Word")