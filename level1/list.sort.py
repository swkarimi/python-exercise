'''
Sort the list by the length of the values.
    
level: 1
'''
words = ['ball', 'student', 'university', 'sport', 'new']
words.sort(key=len)
print(words)

'''
Sort reversed the list by second element in each tuple 
that every tuple has 3 element
    
level: 1
'''
a = [(2, 3, 4), (1,-1, 8), (3, -5, 6)]
def dim(n): return n[1]
a.sort(reverse = True, key=dim)
print(a)

'''
sort the list by sum of element.

level: 1
'''
a = [[2, -1], [-2, 4], [-3, 2]]
a.sort(reverse = True, key=sum)
print(a)
