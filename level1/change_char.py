'''
Write a program to get a string from a given string 
where all occurrences of its first char have been changed to '*',
except the first char itself.

level: 1 
'''

def foo1(s):
    new_s = s[0]
    for i in range(1, len(s)):
        if s[i] == new_s[0]:
            new_s +='*'
        else:
            new_s += s[i]
    return new_s

def foo2(s):
    list_s = list(s)
    for i in range(1,len(s)):
        if s[i] == list_s[0]:
            list_s[i] = '*'
    return ''.join(list_s)

def foo3(s):
    char = s[0]
    s = s.replace(char, '*')
    s = char + s[1:]
    return s


print(foo1('this is a test.'))
print(foo2('this is a test.'))
print(foo3('this is a test.'))
