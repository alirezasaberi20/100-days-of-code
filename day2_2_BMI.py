# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:11:04 2021

@author: Alireza Saberi
"""

weight = int(input("How much do you weigh in Kg? "))
height =float(input("How Tall are you in Meters? "))
BMI= int(weight/(height**2))
print("your BMI is: "+str(BMI))