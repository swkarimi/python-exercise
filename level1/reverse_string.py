'''
Write a program to reverse a string.

level: 1
'''
str1 = 'this is a first test.'
index = len(str1)
str1_reverse = ''
while index > 0:
    index -= 1
    str1_reverse += str1[index]
    
print(str1_reverse)
    

str2 = 'this is a second test.'
str2_reverse = str2[::-1]
print(str2_reverse)
