# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:31:54 2020

@author: vinayt
"""

readme="https://www.hackerrank.com/challenges/find-a-string/problem"

string="TestCaseTestCase"
sub_string="CaseT"

#string="ABCDCDC"
#sub_string="CDC"
z=0
r=0

for i in range(len(string)):
    if string[i] == sub_string[0] and z < (len(string) -1 ):
        z=i
        c=0
        for j in range(len(sub_string)):
            #print(f"string[z] : {string[z]}")
            #print(f"sub_string[j] : {sub_string[j] }")
            if string[z] == sub_string[j]:
                if z < len(string) -1:
                    z=z+1
                else:
                    pass
                c=c+1
        if c == len(sub_string):
            r=r+1

print(f"Total Match: {r}")

