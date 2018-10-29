'''
Write a program to reverse a string word by word.

level: 2
'''
def reverse_words(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)

text1 = 'it is rainy.'
print(reverse_words(text1))
