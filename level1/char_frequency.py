'''
 Write a program to count the number of characters in a string.
 
level: 1
'''

def char_frequency(s):
    chf = dict({})
    for char in s:
        keys = chf.keys()
        if char in keys:
            chf[char] += 1
        else:
            chf[char] = 1
    return chf

print(char_frequency('this is a test.'))
