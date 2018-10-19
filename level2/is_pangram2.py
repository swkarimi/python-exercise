'''
Write a Python function to check a string is a pangram or not.

Hint: A pangram is a sentence using every letter
of a given alphabet at least once.

level: 2
'''

def is_pangram(s):
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z'])
    s = set(s.lower())
    return alphabet <= s

sentence1 = 'The quick brown fox jumps over the lazy dog.'
print(is_pangram(sentence1))

sentence2 = 'The five boxing wizards jump quickly.'
print(is_pangram(sentence2))
        
        