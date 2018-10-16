'''
Write a program to get all possible unique subsets from a set of distinct members

level : 4
'''
def sub_sets(sset):
        return subsetsRecur([], sorted(sset))
    
def subsetsRecur(current, sset):
    if sset:
        return subsetsRecur(current, sset[1:]) + subsetsRecur(current + [sset[0]], sset[1:])
    return [current]

print(sub_sets([4, 2, 9]))