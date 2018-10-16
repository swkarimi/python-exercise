'''
Write a Python class to find the three elements
that sum to zero from a set of n real numbers.

level: 2
'''

def three_sum(nums):
    indices = list()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    indices.append((i, j, k))
    return indices

n = [-5, -1, 4, 2, -2, 6, 3, 1]
print(three_sum(n))