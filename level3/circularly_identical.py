'''
Write a program to check whether two lists are circularly identical.

level: 3
'''
def circularly_identical(a, b):
    aa = ''.join(map(str, a))
    bb = ''.join(map(str, b*2))
    return (aa in bb)

a = [1, 2, 3]
b = [3, 1, 2]
c = [2, 1, 3]
print('Compare list a and list b: ', circularly_identical(a, b))
print('Compare list a and list c: ', circularly_identical(a, c))
