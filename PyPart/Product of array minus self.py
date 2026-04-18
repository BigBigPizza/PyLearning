# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:32:02 2026

@author: Chris
"""

array1 = [1, 2, 3, 4]

def product_of_array_minus_self(array_input):
    n = len(array_input)
    output = [1] * n
    
    left_mult = 1
    for i in range(n):
        output[i] *= left_mult
        left_mult *= array_input[i] 
    
    right_mult = 1
    for i in range(n-1, -1 ,-1):
        output[i] *= right_mult
        right_mult *= array_input[i] 
    
        
    print(output)
    
    
product_of_array_minus_self(array1)
    
        