'''
Write program to generate dictionary in the form {1:1, 2:4, ..., 9:81}
then display them like 5² = 25

level: 1
'''
n = 10
d = dict()

for i in range(1, n):
    d[i] = i*i

for k,v in d.items():
    print('{0}\u00b2 = {1:2d}'.format(k,v))
