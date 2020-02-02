# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:37:57 2020

@author: vinayt
"""
import random

passtype=str(input("What type of password would you like to generate:[strong/medium/weak]"))
passtype.lower()

def passGen(var):
    charlist=["@","+","-","*","!","^","_","(",")"]
    alplist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    password=""
    
    if var == "weak":
        password+=random.choice(alplist).upper()+random.choice(alplist)+str(random.randrange(1,9) *10)+random.choice(alplist)+random.choice(alplist).upper()
    elif var == "medium":
        password+=random.choice(alplist).upper()+random.choice(alplist)+random.choice(charlist)+str(random.randrange(1,9) *10)+random.choice(alplist)+random.choice(alplist).upper()+random.choice(charlist)
    elif var == "strong":
        password+=random.choice(alplist).upper()+random.choice(alplist)+random.choice(charlist)+str(random.randrange(1,9) *10)+random.choice(alplist)+random.choice(charlist)+random.choice(alplist)+random.choice(alplist).upper()+random.choice(alplist)+random.choice(alplist)+random.choice(charlist)+str(random.randrange(1,9) *10)+random.choice(charlist)
    else:
        print("Invalid Input!!")
    return(password)

password=passGen(passtype)
print("Your Password is:",password)        