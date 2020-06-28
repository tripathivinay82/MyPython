# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:39:58 2020

@author: vinayt
"""

readme="https://www.hackerrank.com/challenges/python-lists/problem"

list1=[]
a=[]

for i in range(int(input())):
    a=input().split(" ")
        
    if a[0] == "insert":
        list1.insert(int(a[1]),int(a[2]))
    elif a[0] == "print":
        print(list1)
    elif a[0] == "remove":
        list1.remove(int(a[1]))
    elif a[0] == "append":
        list1.append(int(a[1]))
    elif a[0] == "sort":
        list1.sort()
    elif a[0] == "pop":
        list1.pop()
    elif a[0] == "reverse":
        list1.reverse()
        
        