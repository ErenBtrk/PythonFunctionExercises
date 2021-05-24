'''
13. Write a Python function that prints out the first n rows of Pascal's triangle. 
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

Sample Pascal's triangle :

Pascal's triangle
Each number is the two numbers above it added together 

'''
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 

         





