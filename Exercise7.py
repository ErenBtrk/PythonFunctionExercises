'''
7. Write a Python function that accepts a string and calculate
the number of upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

'''

def function(string):
    lowerCount = 0
    upperCount = 0
    for item in string:
        if(not item.isalpha()):
            continue
        if(item.islower()):
            lowerCount += 1
        else:
            upperCount += 1
    print(f"Lower case count = {lowerCount}")
    print(f"Upper case count = {upperCount}")


string1 = "HeLLO WorlD123 "

function(string1)