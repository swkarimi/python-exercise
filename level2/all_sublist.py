'''
Write a program to generate all sublists of a list.

level: 2
'''

def all_sublist(li):
    subs = [[]]
    for i in range(len(li)):
        for j in range(i, len(li)):
            subs.append(li[i:j+1])
    return subs

li = ['a', 'b', 'c', 'd']
print(all_sublist(li))
