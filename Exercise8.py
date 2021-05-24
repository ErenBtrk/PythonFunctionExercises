'''
8. Write a Python function that takes a list and returns a new list
with unique elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

'''

def function(list1):
    new_list = list(set(list1))
    return new_list

list1 = [1,2,3,3,3,3,4,5]

print(function(list1))
