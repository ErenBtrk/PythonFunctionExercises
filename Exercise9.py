'''
9. Write a Python function that takes a number as a parameter and check
the number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1 
and that has no positive divisors other than 1 and itself.

'''

def function(number):
    if(number < 2):
        return False
    isPrime = True
    for index in range(2,number):
        if(number % index == 0):
            isPrime = False
            break
    return isPrime

print(function(4))
