# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 01:59:36 2026

@author: Ferti
"""

def find_dup_str(s, n):
    for i in range(0, len(s) - n + 1):
        substring = s[i:i + n]
        
        for j in range (i + n, len(s) - n + 1):
            second_substring = s[j: j + n]
            
            if substring == second_substring:
                return substring
    return ""

def find_max_dup(s):
    best = ""
    for n in range (1, len(s)//2 + 1):
        candidate = find_dup_str(s, n)
        if len(candidate) > len(best):
            best = candidate
            
    return best
        