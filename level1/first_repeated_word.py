'''
Write a program to find the first repeated word in a given string.

level: 1
'''

def first_repeated_word(s):
    tmp = set()
    words = s.split()
    for word in words:
        if word in tmp:
            return word
        else:
            tmp.add(word)

print(first_repeated_word('abc bc ab bc ab'))
