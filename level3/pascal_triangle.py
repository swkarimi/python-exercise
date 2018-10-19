'''
Write a function that print the first n rows of Pascal's triangle.

Hint: if n equals 7, function prints like this
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]

level: 3
'''

def pascal_triangle(n):
   trow = [1]
   zero = [0]
   for x in range(n):
       print(trow)
       trow=[l+r for l,r in zip(trow + zero, zero + trow)]

pascal_triangle(10)

