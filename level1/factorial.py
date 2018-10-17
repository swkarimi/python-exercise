'''
Write a function to calculate the factorial of a number (a non-negative integer).

level: 1
'''

def factorial1(n):
    i = 1
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial2(n - 1)

print(factorial1(5))
print(factorial2(6))
