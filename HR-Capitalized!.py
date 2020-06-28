# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:54:22 2020

@author: vinayt
"""

readme="https://www.hackerrank.com/challenges/capitalize/problem"

def cap(s):
    str1=s.rstrip()
    str1=str1.split(" ")
    
    fn=[]
    for i in range(len(str1)):
        fn.append(fun(str1[i]))
    
    return " ".join(fn)

def fun(s):
    
    fn=[]
    c=0
    for i in s:
        if c == 0:
            if i.isalnum() == 'True' and i.isdigit() == 'True':
                continue
            i=i.upper()
            c=c+1
        fn.append(i)
    
    fn="".join(fn)
    return fn
    
def main():
    str1=str(input())
    print(cap(str1))
    

if __name__ == "__main__":
    main()