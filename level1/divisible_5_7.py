'''
Write a program to generate list which are divisible by 5 and 7,
between 1000 and 1200 (both included), then print them.

level: 1
'''

li = [i for i in range(1000, 1201) if i%5==0 or i%7==0]
print(li)


