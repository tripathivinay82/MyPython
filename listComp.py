# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:43:33 2020

@author: vinayt
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list=[""]
new_list.clear()

for i in a:
    for j in b:
        if i != j or i in new_list:
            continue
        else:
            new_list.append(i)
print(new_list)
        
            
        
