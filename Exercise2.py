'''
2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20

'''

def function(list1):
    sum = 0
    for item in list1:
        sum += item
    return sum

list1 = [5,10,15,20,25]

print(function(list1))