# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:38:00 2021

@author: Alireza Saberi
"""
for n in range(1,100):
    if n%3!=0 and n%5!=0:
        print(n)
    if n%15 ==0:
        print("fizzbuzz")
    if n%5==0 and n%3!=0:
        print("buzz")
    if n%3==0 and n%5 !=0:
        print("fizz")
    