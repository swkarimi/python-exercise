'''
Write a program to generate list of prime number
between a and b (a is included but b is not)

'''
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i ==0:
            return False
    return True


def generate_primes(a, b):
    primes = [i for i in range(a,b) if is_prime(i)]
    return primes

print(generate_prime(100,200))