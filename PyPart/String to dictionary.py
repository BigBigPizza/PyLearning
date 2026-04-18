# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:12:22 2026

@author: Chris
"""

question =  "apple, banana apple orange banana apple"

def string_to_dictionary(input_string):
    split_list = input_string.split()
    
    word_dictionary = {}
    
    for word in split_list:
        word = word.lower().strip(".,!?")
        if word in word_dictionary:
            word_dictionary[word] += 1 
        else:
            word_dictionary[word] = 1
    
    return word_dictionary

print(string_to_dictionary(question))