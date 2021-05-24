'''
14. Write a Python function to check whether a string is a pangram or not. 
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

'''

def function(string):
    flag = True
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for item in alphabet:
        if(not item in string):
            flag = False
            break
    return flag


sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "The quick brown fox jumps over the lzy dog"

print(function(sentence1))
print(function(sentence2))