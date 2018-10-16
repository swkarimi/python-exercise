'''
Write a  program to implement pow(base, exponent),
base and exponent are integer.

level: 2
'''

def pow(base, exponent):
    if exponent == 0:
        return 1
    
    if base == 0 or base == 1 or exponent == 1:
        return base
    
    if exponent < 0:
        negative_exponent = True
        exponent = -exponent
    else:
        negative_exponent = False
    
    power = 1
    for _ in range(exponent):
        power *= base
        
    if negative_exponent:
        return 1/power
    
    return power

print(pow(0,0))
print(pow(2,-2))
print(pow(-3,5))