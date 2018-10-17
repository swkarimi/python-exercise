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