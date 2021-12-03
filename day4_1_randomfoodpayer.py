# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:06:24 2021

@author: Alireza Saberi
"""

import random

#number_of_people = int(input("how many names do you want to enter? "))
listofnames = str.split(input("enter name of the groups using ' ,'."))
p=len(listofnames)

random_number = random.randint(1,p)
payer_1 =listofnames[random_number-1]

print(f"{payer_1} should pay for others!")

