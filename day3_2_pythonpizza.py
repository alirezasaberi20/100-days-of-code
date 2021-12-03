# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:13:14 2021

@author: Alirez Saberi
"""
print("welcome to python pizza delivery!")

pizza_size = input("what type of pizza do you want? large(L),Medium(M) or Small(S) .")

add_pepperoni = input("Do you want pepperoni? Y or N  ")

extra_cheese = input("Do you want extra cheese? Y or N ")

if pizza_size =="L":
    bill = 25
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill +=1
    print(f"your total bill is ${bill}.")
if pizza_size =="M" :
    bill = 20
    if add_pepperoni =="Y":
        bill+=3
    if extra_cheese =="Y" :
        bill+=1
    print(f"your total bill is ${bill}.")
if pizza_size =="S":
    bill=15
    if add_pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
        bill+=1
    print(f"your total bill is ${bill}.")