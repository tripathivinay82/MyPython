#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:51:03 2022

@author: vinay
"""
from tabulate import tabulate
import textfsm


with open('show_interface.template') as template, open('show_interface') as interface:
    fsm = textfsm.TextFSM(template)
    header = fsm.header
    result = fsm.ParseText(interface.read())

print(tabulate(result,headers=header))