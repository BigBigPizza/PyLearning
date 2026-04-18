# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:12:41 2026

@author: Chris
"""

nums_list1 = [1, 2, 3, 2, 4, 1, 5]

def repeated_nums(number_list):
    seen = []
    repeats = []
    
    for num in number_list:
        if num in seen and num not in repeats:
            repeats.append(num)
            continue
        seen.append(num)
    return repeats
            
def repeated_nums_sets(number_list):
    seen = set()
    repeats = set()
    
    for num in number_list:
        if num in seen and num not in repeats:
            repeats.add(num)
            continue
        seen.add(num)
    return list(repeats)

print(repeated_nums(nums_list1))
print(repeated_nums_sets(nums_list1))