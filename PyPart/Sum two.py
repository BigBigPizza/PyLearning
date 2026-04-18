# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:19:04 2026

@author: Chris
"""

nums = [19, 45, 2,7,11,15]
target = 9


for ind1 in range(0, len(nums)):
    for ind2 in range(0, len(nums)):
        if ind1 == ind2:
            continue
        result = nums[ind1] + nums[ind2]
        if result == target:
            print (ind1, ind2)
            
            
## Solution 2

def sum_two(numbers_array, target_value):
    seen = {}
    
    for i, num in enumerate(numbers_array) :
        compliment = target_value - num
        print(seen)
        
        if compliment in seen:
            return (i,seen[compliment])
        
        seen[num] = i
    
    return None

sum_two(nums, target)