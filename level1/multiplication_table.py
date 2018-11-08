'''
Write a program to generate the multiplication table in a list,
then print it.

level: 1
'''

table = [[i*j for j in range(1,10)] for i in range(1,10)]

for row in table:
    for num in row:
        print('{:5d}'.format(num), end='')
    print('\n')
