'''
6. Write a Python function to check whether a number is in a given range.
'''

def function(number,startNum,endNum):
    if number in range(startNum,endNum):
        return True
    else:
        return False

startNum = 5
endNum = 21

print(function(10,startNum,endNum))
print(function(3,startNum,endNum))
print(function(22,startNum,endNum))
