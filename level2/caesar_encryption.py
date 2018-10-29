'''
Write a Python to create a Caesar encryption.
 
level: 2
'''

import string

def caesar_encryption(s, shift):
    lc = list(string.ascii_lowercase)
    uc = list(string.ascii_uppercase)
    plain_string = list(s)
    encrypted_string = list()
    for char in plain_string:
        if char in lc:
            new_char = lc[(lc.index(char) + shift) % 26]
        elif char in uc:
            new_char = uc[(uc.index(char) + shift) % 26]
        else:
            new_char = char
        encrypted_string.append(new_char)
    res = ''.join(encrypted_string)
    return res
    
s = "Caesar's code or Caesar shift, is one of the simplest #encryption techniques!."
print(caesar_encryption(s, 3))
    