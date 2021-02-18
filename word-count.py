#!/usr/bin/python3.7

import re

# Option-1 (using function)
#def MyProg(wstr):
#    print({i:len(re.findall(i,wstr)) for i in list(set(wstr.split()))})

# Option-2 (using lambda function)
MyProg = lambda wstr: print({i:len(re.findall(i,wstr)) for i in list(set(wstr.split()))})

wstr = 'it was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness'
MyProg(wstr)