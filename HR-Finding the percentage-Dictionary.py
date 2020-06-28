# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:20:45 2020

@author: vinayt
"""
from decimal import Decimal
readme="https://www.hackerrank.com/challenges/finding-the-percentage/problem"

if __name__ == '__main__':
    
    data={}
    for i in range(int(input())):
        st=str(input())
        st=st.rstrip()
        st=st.split(" ")
        
        name=str(st[0]) ; #name of person
        data[name]={} #Initialize the dict in dict or nested dict
        data[name]['Math']=float(st[1])
        data[name]['Physics']=float(st[2])
        data[name]['Chemistry']=float(st[3])

    name=str(input())
    avg_mark=round(Decimal((data[name]['Math'] + data[name]['Physics'] + data[name]['Chemistry'])/3),2)
    
print(avg_mark)
    
    