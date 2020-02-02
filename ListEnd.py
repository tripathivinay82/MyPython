# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:34:21 2020

@author: vinayt
"""

list1=input("Enter The numbers for list:")

new_list=[""]
new_list.clear()

new_list.append(list1[0])
new_list.append(list1[-1])

print("Here is the new list:", new_list)