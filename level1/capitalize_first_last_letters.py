'''
Write a program to capitalize first and last letters 
of each word of a given string.

level: 1
'''

def capitalize_first_last_letters(s):
     result =  str()
     for word in s.split():
        result += word[0].upper() + word[1:-1] + word[-1].upper() + ' '
     return result
     
print(capitalize_first_last_letters('to capitalize first and last letters'))