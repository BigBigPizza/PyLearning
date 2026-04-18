# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:39:16 2026

@author: Chris
"""

random_number = 13


def number_to_roman_numerals(number_to_convert):
    roman_numeral_list = [
        ("X", 10),
        ("V", 5),
        ("I", 1)
        ]
    numeral = ""
    for entry in roman_numeral_list:
        while number_to_convert >= entry[1]:
            if number_to_convert == 9:
                numeral += "IX"
                return numeral
            if number_to_convert == 4:
                numeral += "IV"
                return numeral
            numeral += entry[0]
            number_to_convert -= entry[1]
    return numeral


print(number_to_roman_numerals(random_number))
    