'''
Write a function to sum all the numbers in a list.

level: 1
'''

def sum_of_list(nums):
    total = 0
    for val in nums:
        total += val
    return total

list1 = [1, 4, -2, 5, 6, 11]
print(sum_of_list(list1))
