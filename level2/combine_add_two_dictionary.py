''''
Write a program to combine two dictionary adding values for common keys.

level: 2
'''
d1 = {'a': 5, 'c': 8, 'd':2, 'b': 4}
d2 = {'a': 1, 'b': 3, 'e':4, 'd': 7, 'f': 1}

d3 = {}
for key1 in d1.keys():
    if key1 in d2.keys():
        # update d3 by sumition values with common keys
        d3.update({key1:d1[key1]+d2[key1]})
    else:
        # update d3 by items that have unique key from d1
        d3.update({key1:d1[key1]})

for key2 in d2.keys():
    if key2 not in d1.keys():
        # update d3 by items that have unique key from d2
        d3.update({key2: d2[key2]})

# sort d3 by keys
d3 = dict(sorted(d3.items(), key=lambda n:n[0]))
print(d3)
