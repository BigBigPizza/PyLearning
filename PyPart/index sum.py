# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:24:14 2026

@author: Chris
"""

nums = [2, 7, 11, 15]
tar = 9

def index_sums(num_list, target):
    seen = {}
    for i, num in enumerate(num_list):
        finder = target - num
        if finder in seen:
            return [seen[finder], i]
        else:
            seen[num] = i
            
print(index_sums(nums, tar))