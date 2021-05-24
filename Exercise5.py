'''
5. Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
'''

def function(num):
    factorial = 1
    for index in range(2,num+1):
        factorial *= index
    return factorial


print(function(3))