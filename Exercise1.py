'''
1. Write a Python function to find the Max of three numbers.
'''

def function(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    elif(num3>num1 and num3>num2):
        return num3
    
number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))
number3 = int(input("Please enter a number : "))

print(function(number1,number2,number3))