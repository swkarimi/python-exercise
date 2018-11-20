'''
Write a  program to insert a given string
at the beginning of all items in a list.

level: 1
'''
x = [1,2,3,4,5]
s = 'a'
sx = [s + str(item) for item in x]
print(sx)
