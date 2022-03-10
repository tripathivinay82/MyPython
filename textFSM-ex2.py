#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:30:16 2022

@author: vinay
"""
from tabulate import tabulate
import textfsm

time = "15:10:44.867 UTC Sun Nov 13 2016"


with open('template2.template',mode='r') as hd:
    fsm = textfsm.TextFSM(hd)
    res = fsm.ParseText(time)
    header = fsm.header
    
print(tabulate(res, headers=header))