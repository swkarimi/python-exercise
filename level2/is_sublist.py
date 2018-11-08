'''
Write a program to check whether a list contains a sublist.

level: 2
'''

def is_sublist(subli ,li):
    if len(subli) == 0 or subli == li:
        return True
    if len(subli) > len(li):
        return False
    for i in range(len(li)):
        if subli == li[i:i+len(subli)]:
            return True
    return False

     
l1 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 4, 5]
l2 = [4,5,6]

print(is_sublist(l2, l1))