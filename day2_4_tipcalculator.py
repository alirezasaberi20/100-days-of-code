# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:42:00 2021

@author: Alireza Saberi
"""
total_bill = float(input("what was the total Bill? $"))

tip_percentage = int(input("what percentage tip do you want to give? "))

people_number = int(input("how many people do you want to split? "))

share = (total_bill*(100+tip_percentage))/(people_number*100)

share=round(share, 2)

print(f"each person should pay {share}$.")
