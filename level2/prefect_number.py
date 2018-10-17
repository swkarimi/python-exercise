'''
Write a program to print all prefect number under 1000.

level: 2

Hint: Perfect number, a positive integer that is 
equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Other perfect numbers are 28, 496, and 8128.
'''

def is_prefect_number(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if n == s:
        return True
    return False

for i in range(1, 1000):
    if is_prefect_number(i):
        print(i)
        