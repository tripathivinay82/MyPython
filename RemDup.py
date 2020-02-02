# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:40:47 2020

@author: vinayt
"""

def removeDup(list_name):
    new_list=[]
    for a in range(len(list_name)):
        if list_name[a] in new_list:
            print("%s exists in new list..hence skipping..." %list_name[a])
        else:
            new_list.append(list_name[a])
            print(new_list)
    return(new_list)
    
def remDupSet(list_name):
    return list(set(list_name))    
list_name=[1,2,2,3,4,3,5,6,6,7]

new_list=removeDup(list_name)

new_list_set=remDupSet(list_name)

print("New list is:", new_list)
print("New list using set is:", new_list_set)
    