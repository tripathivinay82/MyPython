# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:48:27 2020

@author: vinayt
"""

readme="https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"

def print_formatted(number):
    for i in range(1,n + 1):
        pad = n.bit_length()
        print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)