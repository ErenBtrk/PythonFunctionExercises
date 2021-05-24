'''
12. Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as 
forward, e.g., madam or nurses run.

'''

def function(string1):
    reversedString = ""
    for index in range(-1,len(string1)*-1-1,-1):
        reversedString += string1[index]
    
    if(reversedString == string1):
        return True
    else:
        return False

print(function("madam"))
print(function("yarasa"))
print(function("anastasmumsatsana"))
