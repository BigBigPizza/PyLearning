# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:59:19 2026

@author: Chris
"""

nums1 = "aabbcde"
nums2 = "aabbcc"

nums3 = "a a b b c"
nums4 = "AabBc"

def first_non_repeating_character(repeat_string):
    seen = {}
    
    for char in repeat_string.lower().strip():
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for key, value in seen.items():
        if value == 1:
            return key
    return -1

        
    
        
print(first_non_repeating_character(nums1))
print(first_non_repeating_character(nums2))
print(first_non_repeating_character(nums3))
print(first_non_repeating_character(nums4))