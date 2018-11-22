'''
Write a program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

leve: 1
'''
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
d = dict(zip(keys,values))
print(d)