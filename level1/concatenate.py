'''
Write a Python program to create a list by concatenating a given list
which range goes from 1 to n.

level: 1
'''

li = list(['Bob', 'Alice', 'John', 'Mary'])
n = 3

res = ['{}{}'.format(item,i) for item in li for i in range(1, n+1)]

print(res)