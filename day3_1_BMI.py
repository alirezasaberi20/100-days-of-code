# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:16:40 2021

@author: Alireza Saberi
"""
height = float(input("what is your height in meters? "))
weight = float(input("how much do you weigh? "))
BMI = weight/(height**2)

if BMI < 18.5:
    print("you are underweight!")
elif  BMI<25:
    print("you are normal weight!")
elif BMI<30:
    print("you are overwight!")
elif BMI<35:
    print("you are obese!")
else:
    print("you are cilinically obese!")
    
  

