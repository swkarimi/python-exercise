'''
Write a program to find validity of a string of parentheses,
'(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()", "()[]{}" and "{()}[]" are valid but "[)", "({[)]" and "{{{" are invalid.

level: 2
'''
def string_is_correct(s):
    stack = list()
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            upon_stack_char = stack.pop()
            if char == ')' and upon_stack_char != '(':
                return False
            if char == ']' and upon_stack_char != '[':
                return False
            if char == '}' and upon_stack_char != '{':
                return False
    if len(stack) != 0:
        return False
    return True
       
s = '{{}}()(())('
print(string_is_correct(s))
    