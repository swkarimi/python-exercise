'''
Write a program to find the second largest number in a list.
 
level: 1
'''

def second_largest_number(nums):
    if len(nums) < 2:
        return None
    if len(nums) >= 2:
        if nums[0] < nums[1]:
            first_largest = nums[1]
            second_largest = nums[0]
        else:
            first_largest = nums[0]
            second_largest = nums[1]

    for num in nums[2:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num

    return second_largest

n =[644, 120, 141, 342, 8, 612, 786, 885, 418, 815,
    391, 519, 444, 112, 175, 427, 730, 613, 700, 937]

print(second_largest_number(n))
