'''
Write a program to find all pair of elements (indices of the two numbers)
from a given array whose sum equals a specific target number.

level: 2
'''

def two_sum(nums, goal_num):
    indices = list()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == goal_num:
                indices.append((i, j))
    return indices

n = [3, 1, 6, 2, 1, 8, 3]
g = 9
print(two_sum(n, g))
