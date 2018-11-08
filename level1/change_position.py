'''
Write a program to change the position of every n-th value
with the (n+1)th in a list.

level: 1
'''
nums = [1, 2, 3, 4, 5, 6, 7]
res=[]
for i in range(0,len(nums),2):
    if i+1 < len(nums):
        res.append(nums[i+1])
    res.append(nums[i])

print(res)
