# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:57:13 2021

@author: Alireza Saberi
"""
import random
print("welcome to guess number game!\n")
print("I'm thinking between 1 to 100")
game_level  = input("choose your game level as 'hard' or 'easy': ")
number = random.randint(1,100)

if game_level =="hard":
    for i in range(1,6):
        guess = int(input(f"enter your {6-i} chances out of 5: "))
        if guess == number:
            print("it's totally true!")
            break
        elif i==6 and number != guess:
            print("Game over!")
        elif guess> number:
            print("it is too high!")
           
        elif guess <number:
            print("it's too low!")
           
        
            
if game_level =="easy":
    for i in range(1,11):
        guess = int(input(f"enter your {11-i} chances out of 10: "))
        if guess == number:
            print("it's totally true!")
            break
        elif guess> number:
            print("it is too high!")
           
        elif guess <number:
            print("it's too low!")
          
        elif i==11 and guess != number:
            print("Game over!")
            
