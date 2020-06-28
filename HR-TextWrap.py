# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:48:01 2020

@author: vinayt
"""

import textwrap

def wrap(string, max_width): 
    return textwrap.fill(string, max_width)
    
if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width=4
    result = wrap(string, max_width)
    print(result)