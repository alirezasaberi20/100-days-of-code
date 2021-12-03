# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:27:55 2021

@author: Alireza Saberi
"""
age = int(input("How old are you? "))
left_years = 90-age
left_months= left_years*12
left_weeks = left_years*52
left_days = left_years*365
print(f"you have {left_days} days,{left_weeks} weeks and {left_months} Months!")

