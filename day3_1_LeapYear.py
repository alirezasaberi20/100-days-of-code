# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:37:28 2021

@author: Alireza Saberi
"""
year = int(input("enter the year: "))

if year%4==0:

    if year%100!=0:
        print("Leap Year!")
    elif year%400==0:
        print("Leap year")

else:
    print("Not Leap year!")
