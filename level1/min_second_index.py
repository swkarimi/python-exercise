'''
Write a program to find a tuple,
the smallest second index value from a list of tuples.

level: 1
'''

x = [(17, 19), (20, 8), (6, 6), (11, 5), (1, 14),
     (6, 10), (0, 11), (1, 7), (17, 0), (2, 16)]

x_min = min(x, key = lambda n: n[1])
print(x_min)
