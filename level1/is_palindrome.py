'''
Write a function that checks a string is palindrome or not.

Hint: A palindrome is a string that reads
the same backward as forward, e.g., madam.

level: 1
'''

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

print(is_palindrome('test')) # False
print(is_palindrome('Level')) # True
