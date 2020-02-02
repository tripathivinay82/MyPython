# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:16:55 2020

@author: vinayt
"""


var1=str(input("Enter the string:"))
var1=var1.split(" ")
print("Entered String in List Format",var1)

def revString(in_str):

    
    c1=len(in_str)-1
    new_list=[]
    for a in range(len(in_str)):
        new_list.append(in_str[c1])
        c1=c1-1
    return(new_list)
    
var1=revString(var1)
var1=" ".join(var1)
print("Output String is:",var1)
        

