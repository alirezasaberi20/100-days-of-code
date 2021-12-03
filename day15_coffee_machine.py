# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:03:36 2021

@author: Alireza Saberi
"""

machine_working = False

MENU = {
        "espersso":
        {
        "ingredients":
            {
            "water":50,
            "coffee":18,
            },
            "cost":1.5,},
        
        "latte":
            {
                "ingredients":{
                    "water":200,
                    "coffee":24,
                    "milk":150
                    },
                "cost":2.5,
                },
            "cappuccino":
                {
                "ingredients":
                    {
                        "water":250,
                        "coffee":24,
                        "milk":100
                    },
                "cost":3
                }
        
        }
    
Resources = {
    "water":10000,
    "milk":5000,
    "coffee":400,
    "money":57.5
            }

  
while not machine_working:
    answer = input("what do you like? , 'espersso' , 'latte','cappuccino'.").lower()
    if answer == "report":
        water_sum = Resources["water"]
        milk_sum = Resources["milk"]
        coffee_sum = Resources["coffee"]
        money_sum =Resources["money"]
        print(f"remaning water is {water_sum}")
        print(f"remaning milk is {milk_sum} ")
        print(f"remaning coffee is {coffee_sum} ")
        print(f"remaning money is ${money_sum}")
    
    elif answer == "espersso":
        if Resources["water"] >= MENU["espersso"]["ingredients"]["water"] and Resources["coffee"] >= MENU["espersso"]["ingredients"]["water"]:
            entered_money = float(input("enter $1.5 for your order. ")) 
            if entered_money >= 1.5:
                Resources["money"] = Resources["money"] + 1.5
                change = round(entered_money - 1.5, 2)
                Resources["water"]  -= MENU["espersso"]["ingredients"]["water"]
                Resources["coffee"] -= MENU["espersso"]["ingredients"]["water"]
            
                print(f"{change} as refund.")
                print("your order is ready!")
            else:
                print("Not sufficient money!")
                
    elif answer == "latte":
        
        if (Resources["water"] >= MENU["latte"]["ingredients"]["water"] and Resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]) and Resources["milk"]>= MENU["latte"]["ingredients"]["milk"] :
            entered_money = float(input("enter $2.5 for your order. ")) 
            if entered_money >= 2.5:
                    Resources["money"] = Resources["money"] + 2.5
                    change = round(entered_money - 2.5,2)
                    Resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    Resources["coffee"] -=MENU["latte"]["ingredients"]["coffee"]
                    Resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    print(f"{change} as refund.")
                    print("your order is ready!")
            else:
                print("Not sufficient money!")
                    
    elif answer == "cappuccino":
        
        if (Resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and Resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]) and Resources["milk"]>= MENU["cappuccino"]["ingredients"]["milk"] :
            entered_money = float(input("enter $3 for your order. ")) 
            if entered_money >= 3:
                    Resources["money"] = Resources["money"] + 3
                    change = round(entered_money - 3,2)
                    Resources["water"]  -= MENU["cappuccino"]["ingredients"]["water"]
                    Resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    Resources["milk"]   -= MENU["cappuccino"]["ingredients"]["milk"]
                    print(f"{change} as refund.")
                    print("your order is ready!")
            else:
                print("Not sufficient money!")
                    
                    
    elif answer == "off" :
        machine_working = True
    
