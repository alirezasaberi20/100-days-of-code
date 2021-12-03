# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:45:13 2021

@author: Alireza Saberi
"""
number = int(input("Enter a Number Plaese: "))
             
remained =number % 2
if remained==1:
    print(f"{number} is odd!")
else:
    print(f"{number} is even!")
