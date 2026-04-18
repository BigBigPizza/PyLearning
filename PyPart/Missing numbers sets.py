# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:24:12 2026

@author: Chris
"""

nums_list1 = [4, 3, 2, 7, 8, 2, 3, 1]

def missing_nums(number_list):
    list_length = len(number_list)
    all_nums = set()
    missing_nums = set()
    
    for num in range(1, list_length):
        all_nums.add(num)
    
    for num in all_nums:
        if num not in number_list:
            missing_nums.add(num)
    
    return list(missing_nums)

def better_missing_nums(number_list):
    list_length = len(number_list)
    all_nums = set(range(1, list_length))
    numbers_set = set(number_list)
    
    return list(all_nums - numbers_set)
        

print(missing_nums(nums_list1))
print(better_missing_nums(nums_list1))