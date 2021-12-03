ending = False
def calculator(x,y,operator):
    if operator == '+':
        return x+y
    elif operator =='-':
        return x-y
    elif operator =='*':
        return x*y
    elif operator =="/":
        if y == 0:
            return "Not Defined!"
        else:
            return x/y
    




while not ending:
    
    first_digit = float(input("Enter Your first Digit: "))
    operator = input("Choose your opearator:\n +\n - \n * \n / \n")
    second_digit = float(input("Choose your Second Digit: "))
    answer = calculator(first_digit,second_digit,operator)
    print(f"{answer} ")
    keep_on = input("Do you want to keep on?(Enter y/n)").lower()
    if keep_on =='n':
        ending = True
    
            
                
            
            
            
            
            
            
            