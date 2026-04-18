# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:15:11 2026

@author: Chris
"""

s = "abcabcbb"

def longest_substring(full_string):
    seen = []
    
    longest_count = 0
    current_count = 0
    
    for char in full_string:
        if char in seen:
            seen = [char]
            current_count = 1
        else:
            seen.append(char)
            current_count += 1
            longest_count = max(longest_count, current_count)
    
    return longest_count
            
print(longest_substring(s))
    
def better_longest_substring(full_string):
    seen = []
    left = 0
    
    longest_count = 0
    for char in full_string:
        if char in seen:
            seen.remove(full_string[left])
        else:
            seen.append(char)
            
            