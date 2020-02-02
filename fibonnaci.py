# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:34:46 2020

@author: vinayt
"""



def fibannoci():
    num=int(input("Enter the total fibonnci numbers needs to be generated.."))
    fib=[]
    if num == 0:
        fib=[]
    elif num == 1:
        fib=[1]
    elif num == 2:
        fib=[1,1]
    else:
        i=1
        fib=[1,1]
        print(fib)
        while i <= num:
            fib.append(fib[i]+fib[i-1])
            i=i+1
            print(fib)
            
fibannoci()       