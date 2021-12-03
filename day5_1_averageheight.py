# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:46:13 2021

@author: Alireza Saberi
"""
student_height = input("Enter the students height: ").split()
number = len(student_height)
sum =0
for n in range(0, len(student_height)):
    student_height[n]=int(student_height[n])
    sum +=student_height[n]
    
average_height = round(sum/number,2)

print(f"the average height of students is {average_height}.")