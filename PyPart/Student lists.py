# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:30:53 2026

@author: Chris
"""

student_list = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

student_dictionary = {}


for pair in student_list:
    student_name = pair[0]
    student_number = pair[1]
    student_dictionary[student_name] = student_number

print(student_dictionary)

def get_student_value(student_name_lookup):
    if student_name_lookup in student_dictionary:
        return student_dictionary[student_name_lookup]
    else:
        return "Student not found"

print(get_student_value("Bob"))
print(get_student_value("Jack"))