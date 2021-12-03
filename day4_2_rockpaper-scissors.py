# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:51:45 2021

@author: ALIREZA SABERI
"""
import random
player1 = input("Rock,paper,scissors: ").lower()

computer = random.randint(0,2)

if player1=="rock":
    player1 = 0
elif player1=="paper":
    player1=1
else:
    player1=2
    
if player1==0:
   if computer==0:
     print("draw")
   if computer==1:
     print("comp wins")
   if computer==2:
     print("player1 wins")
            
if player1==1:
   if computer==0:
     print("player1 wins")
   if computer==1:
     print("draw")
   if computer==2:
     print("computer wins")

if player1==2:
   if computer==0:
     print("comp wins")
   if computer==1:
     print("player1 wins")
   if computer==2:
     print("draw")            