'''
Write a program to count the number of elements in a list
within a specified range.

level: 1
'''

def count_numbers_in_range(nums, min, max):
    n = 0
    for num in nums:
        if min < num < max:
            n += 1
    return n

li = [29, 77, 54, 95, 60, 26, 78, 22, 21,
      12, 15, 36, 69, 43, 3, 18, 24, 67]

print(count_numbers_in_range(li, 20, 40))