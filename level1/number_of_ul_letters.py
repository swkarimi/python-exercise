'''
Write a Python function that accepts a string and calculate 
the number of upper case letters and lower case letters.

level: 1
'''
# number of upper case letters or lower case letters
def number_of_ul_letters(s):
    res = {'uc':0, 'lc':0}
    for letter in s:
        if letter.isupper():
            res['uc'] += 1
        if letter.islower():
            res['lc'] += 1
    return res

s = 'Hello! Bob.'
a = number_of_ul_letters(s)
print('Number of upper case letter: {0:d}'.format(a['uc']))
print('Number of lower case letter: {0:d}'.format(a['lc']))
