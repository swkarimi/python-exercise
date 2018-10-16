'''
Write a function to find the Max of three numbers.

level: 1
'''
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

a = -5
b = 7
c = 2

print(max_of_three(a, b, c)) 
