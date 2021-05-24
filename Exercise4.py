'''
4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"

'''

def function(string1):
    reversedString = ""
    for index in range(-1,len(string1)*-1-1,-1):
        reversedString += string1[index]
    return reversedString

string1 = "1234abcd"

print(function(string1))
