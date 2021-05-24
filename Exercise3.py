'''
3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336

'''

def function(list1):
    total = 1
    for item in list1:
        total *= item
    return total

list1 = [1,2,3,4,5]

print(function(list1))