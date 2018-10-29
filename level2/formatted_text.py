'''
Write a program to remove existing indentation from all of the lines,
then add a prefix '>>' to all of the lines in a given text,
and display formatted text width equal 40 as output.

level: 2
'''
import textwrap
text = '''
    Python is an interpreted high-level programming language
    for general-purpose programming. Created by Guido van Rossum and
    first released in 1991,Python has a design philosophy that
    emphasizes code readability, notably using significant whitespace.
    It provides constructs that enable clear programming on both small and large scales.
    '''
#text = text.strip()
formatted_text = textwrap.dedent(text)
formatted_text = textwrap.fill(formatted_text, width=38)
formatted_text = formatted_text.strip()
formatted_text = textwrap.indent(formatted_text,'>>')
print(formatted_text)