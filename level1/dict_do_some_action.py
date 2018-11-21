'''
Write program to do under instruction
1. concatenate two dictionary a and b
2. remove item that key is divisible by 3
3. get sum of remainder value in dictionary

a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
b = {10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

level: 1
'''
a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
b = {10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

c= dict()
c.update(a)
c.update(b)

for key in list(c.keys()):
    if key % 3 == 0:
        del c[key]

print(sum(c.values()))
