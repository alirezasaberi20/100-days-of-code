# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:06:52 2021

@author: Alireza Saberi
"""
student_score = input("enter the students score: ").split()

for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
    
max_score = student_score[0]
for scores in student_score:
    if max_score<scores:
       max_score =scores 
       
       

print(f"max score is {max_score}.")