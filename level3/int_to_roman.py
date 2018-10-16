'''
Write a program to convert an integer to a roman numeral.

level : 3
'''

def int_to_Roman(num):
    val = [0, 1, 2, 3, 4, 5,
           6, 7, 8, 9, 10,
           20, 30, 40, 50,
           60, 70, 80, 90, 100,
           200, 300, 400, 500,
           600, 700, 800, 900, 1000,
           2000, 3000]

    syb =['', 'I', 'II', 'III', 'IV', 'V',
          'VI', 'VII', 'VIII', 'IX', 'X',
          'XX', 'XXX', 'XL', 'L',
          'LX', 'LXX', 'LXXX', 'XC', 'C',
          'CC', 'CCC', 'CD', 'D',
          'DC', 'DCC', 'DCCC', 'CM', 'M',
          'MM', 'MMM']
    
    num_to_syb = dict(zip(val, syb))
    
    thousands = num // 1000
    hundreds = (num % 1000) // 100
    tens = (num % 100) // 10
    ones = num  % 10
    
    roman_num = ''
    roman_num += num_to_syb[thousands * 1000]
    roman_num += num_to_syb[hundreds * 100]
    roman_num += num_to_syb[tens * 10]
    roman_num += num_to_syb[ones]
    
    return roman_num


num = int(input('Enter a integer number(<4000):'))
print(num,' = ', int_to_Roman(num))


'''
---- Alternative solution 1 ----
def int_to_Roman(num):
    val = [1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,1]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
    
    
---- Alternative solution 2 ----
def int_to_Roman(num):
    roman_num = ''
    while num > 0:
        if num % 1000 == 0:
            roman_num += 'M'
            num -= 1000
        elif num % 1000 == 900:
            roman_num += 'MC'
            num -= 900
        elif num % 500 == 0:
            roman_num += 'D'
            num -= 500
        elif num % 500 == 400:
            roman_num += 'DC'
            num -= 400
        elif num % 100 == 0:
            roman_num += 'C'
            num -= 100
        elif num % 100 == 90:
            roman_num += 'CX'
            num -= 90        
        elif num % 50 == 0:
            roman_num += 'L'
            num -= 50
        elif num % 50 == 40:
            roman_num += 'LX'
            num -= 40
        elif num % 10 == 0:
            roman_num += 'X'
            num -= 10
        elif num % 10 == 9:
            roman_num += 'XI'
            num -= 9
        elif num % 5 == 0:
            roman_num += 'V'
            num -= 5
        elif num % 5 == 4:
            roman_num += 'VI'
            num -= 4
        else:
            roman_num += 'I'
            num -= 1
    roman_num = roman_num[::-1]
    return roman_num
'''