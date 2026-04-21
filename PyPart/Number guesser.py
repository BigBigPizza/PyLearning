# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:28:22 2026

@author: Chris
"""

import random

def start_user_interface():
    
    print("For this game, you will guess a random number between 0 and 100\n")
    print("The computer will then try and guess your answer based on your response\n")
    print("Respond with either 'too low' or 'too high' dependant on the computers guess")
    print("Type 'correct' if the computers answer was correct.")
    print(" ")
    input_y_n = input("Type y to start: ")
    
    while input_y_n.lower() == "y":
        number_guesser_vs_computer()
        input_y_n = input("Would you like to go again? ")
    
    print("Quitting...")


def number_guesser_vs_computer():

    def get_new_guess(lower_bound, upper_bound):
        computer_guess = random.randint(lower_bound, upper_bound)
        return computer_guess
    
    def ask_user():
        print(f"I guess that your number is {computer_guess}, was my guess too low, too high or was it correct?")
        response = input()
        return response.lower()
    
    upper_limit = 100
    lower_limit = 0
    
    computer_guess = get_new_guess(lower_limit, upper_limit)
    response = ask_user()
    
    while response != "correct":
        if response == "too high":
            upper_limit = computer_guess
            computer_guess = get_new_guess(lower_limit, upper_limit)

        elif response == "too low":
            lower_limit = computer_guess
            computer_guess = get_new_guess(lower_limit, upper_limit)

        elif response == "quit":
            break
        
        else:
            print("Please enter either 'too low', 'too high' or 'correct'.")
            
        response = ask_user()
    
    print(f"Your number was {computer_guess}!")
    return
    
        
start_user_interface()





