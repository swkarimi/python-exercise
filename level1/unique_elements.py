'''
Write a Python function that takes a list and 
returns a new list with unique elements of the first list.

level: 1
'''

def unique_elements(nums):
    nums_unique =list()
    for num in nums:
        if num not in nums_unique:
            nums_unique.append(num)
    return nums_unique

a = [3, 2, 3, 1, 5, 4, 1, 2, 6, 0]
unique_a = unique_elements(a)
print(unique_a)
