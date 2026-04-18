# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:46:39 2026

@author: Chris
"""


def find_second_max(num_list):
    largest = num_list[0]
    second_largest = num_list[0]
    
    for num in num_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
            
    return second_largest




print(find_second_max([3, 7, 2, 9, 5]))