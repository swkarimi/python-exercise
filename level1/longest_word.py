'''
write a program that return longest word in a list of words.

level: 1
'''

def longest_word(words):
    index_longest_word = 0
    length_longest_word = 0
    for i, word in enumerate(words):
        len_word = len(word)
        if len_word > length_longest_word:
            length_longest_word = len_word
            index_longest_word = i
    return words[index_longest_word]

words = ['Joyful', 'Tenderness', 'Helpless', 'Defeated', 'Rageful']
print(longest_word(words))