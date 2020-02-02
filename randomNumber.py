# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:26:45 2020

@author: vinayt
"""

import random 

#var1=int(input("Enter your Guess Number[1-9]:"))
act_num=random.randint(1,9)

while True:
    var1=int(input("Enter your Guess Number[1-9]:"))
    if var1 == act_num:
        print("You Guessed is right!! Number is:" + str(act_num))
        break;
    elif var1 > act_num:
        print("Your Guess is higher!!")
    elif var1 < act_num:
        print("Your Guess is low!!")
    elif var1 > 9:
        print("You entered invalid number..it must be within 1-9")
        
