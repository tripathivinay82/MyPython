# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:18:22 2020

@author: vinayt
"""

readme ="https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen"
 
#Only consonents 
def stuartString(string):
    vowel=['A','E','I','O','U']
    string=list(string)
    s1=string.copy()
    
    for a in range(len(string)):
        if string[a] in vowel:
            s1.remove(string[a])
        else:
            return listToStr(s1)
    
#Only vowels         
def kevinString(string):
    vowel=['A','E','I','O','U']
    string=list(string)
    s1=string.copy()
    
    for a in range(len(string)):
        if string[a] in vowel:
            return listToStr(s1)
        else:
            s1.remove(string[a])

# Convert List to string
def listToStr(s):
    s1=''
    for i in range(len(s)):
        s1=s1+s[i]
    
    return s1

#Generate all word combos for Suart
def sWordGen(s):
    wList=[]
    s1=s
    #s=list(s)
    
    while s:  
        wList.extend([s[:i+1] for i in range(len(s))])
        print(f"string: {s}")
        print(f"Type: {type(s)}")
        s=s.replace(s[0],'')
        #s.remove(s[0])
        print(f"string: {s}")
        if s:
            s=stuartString(s)
        else:
            continue
        print(f"string: {s}")
    
    print(f"Stuart's string: {wList}")
    
    #return sum([s1.count(wList[i]) for i in range(len(wList))])
    return sum([occurrences(s1,wList[i]) for i in range(len(wList))])
    
#Generate all word combos for Kevin
def kWordGen(s):
    wList=[]
    s1=s
    #s=list(s)
    
    while s:  
        wList.extend([s[:i+1] for i in range(len(s))])
        print(f"string: {s}")
        s=s.replace(s[0],'')
        #s.remove(s[0])
        print(f"string: {s}")
        if s:
            s=kevinString(s)
        else:
            continue 
        print(f"string: {s}")
           
    print(f"Kevin's string: {wList}")
    
    #return sum([s1.count(wList[i]) for i in range(len(wList))])
    return sum([occurrences(s1,wList[i]) for i in range(len(wList))])
    
def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
        
def main():
    
    string=str(input())
    string=string.rstrip()
    string=string.upper()
    
    sStr=stuartString(string)
    print(f"Stuart's string: {sStr}")
    
    kStr=kevinString(string)
    print(f"Kevin's string: {kStr}")
    
    # Generate the words for both
    sVal=sWordGen(sStr)
    kVal=kWordGen(kStr)
    
    if sVal > kVal:
        print(f"Stuart {sVal}")
    elif kVal > sVal:
        print(f"Kevin {kVal}")
    elif kVal == sVal:
        print("DRAW")

if __name__ == "__main__":
    main()