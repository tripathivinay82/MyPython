#!/usr/bin/python3.7

import re

#This function can check sentence or word palindrome

#Option#1: Using Ternary if-else expression
#def MyDef(sent):
#    print('Sentence is no palindrome') if re.sub('\W|_','',sent).lower() == re.sub('\W|_','',sent).lower()[::-1] else print('Sentence is a palindrome')

#Option#2:  Using Lambda function
MyDef = lambda sent : print('Sentence is a palindrome') if re.sub('\W|_','',sent).lower() == re.sub('\W|_','',sent).lower()[::-1] else print('Sentence is no palindrome')

#sent = "Too hot to hoot." # Palindrome sentence
sent = "Abc def ghi jklm." # no palindrome sentence
#sent = 'boab'

#Execute the function
MyDef(sent)
