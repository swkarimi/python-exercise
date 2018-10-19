'''
Write a program to execute a string containing Python code.

level: 2
'''
code_string = '''
def plus_one(n):
    return n + 1

print(plus_one(3))
'''

exec(code_string)
