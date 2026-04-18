# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:50:06 2026

@author: Chris
"""

palin1 = "radar"
palin2 = "hello"

def palindrome_checker(palin_string):
    palin_length = len(palin_string.lower().strip()) - 1
    palin_reversed = ""
    
    for i in range(palin_length, -1, -1):
        palin_reversed += palin_string[i]
    
    if palin_string == palin_reversed:
        return True
    return False
        
print(palindrome_checker(palin1))
print(palindrome_checker(palin2))
