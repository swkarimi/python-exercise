'''
Write a program to convert a roman numeral to an integer.

level: 2
'''
def roman_to_int(roman_num):
    syb_to_val = {'I':1, 'V':5, 'X':10, 'L':50,
                  'C':100, 'D':500, 'M':1000}
 
    i = 0
    num = 0
    for i in range(len(roman_num)):
        if (syb_to_val[roman_num[i]] > syb_to_val[roman_num[i - 1]]) and i != 0:
            num -= (2 * syb_to_val[roman_num[i - 1]])
        num += syb_to_val[roman_num[i]]
        
    return num

s = input('Enter roman number:')
print(roman_to_int(s))