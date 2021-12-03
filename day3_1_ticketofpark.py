# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:55:05 2021

@author: Alireza Saberi
"""
age  = int(input("how old are you? "))
height = float(input("what is your height in cm? "))

if height <=120:
    print("sorry , due to height limitation , it is impossible to use this.")
else:
    if age<12:
        print("you must pay 5$ for each ticket!")
    if age<=18 & age>=12:
        print("you must pay 7$ for each ticket!")
    if age>=18:
        print("you must pay 12$ for each ticket!")
       