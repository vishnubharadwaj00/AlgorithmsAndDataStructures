# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:13:28 2020

@author: Vishnu
"""

def longestpalindrome(s):
    res=""
    for i in range(0,len(s)):
        tmp=middleout(s,i,i) #case1 babab
        if len(tmp) > len(res):
            res=tmp
        tmp=middleout(s,i,i+1) #case2 babba
        if len(tmp) > len(res):
            res=tmp
    return res

def middleout(s,left,right):
    while(left>=0 and right<len(s) and s[left]==s[right]):
        left-=1
        right+=1
    return s[left+1:right]


s="basasasasdasdasdsdas"
res=longestpalindrome(s)
print(res)
            