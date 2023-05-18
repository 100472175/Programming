""""""
Exercise 8
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Write a program that asks the user to enter a sentence. Then, it introduces each character of the
 sentence in a tuple, ignoring the repeated characters. The characters introduced in the tuple should be capitalized
  (you can use the upper() method of strings). Finally, it prints the tuple. For instance:
   Write a sentence: Hi, how are you? --> (’H’, ’I’, ’,’, ’ ’, ’O’, ’W’, ’A’, ’R’, ’E’, ’Y’, ’U’, ’?’)
"""
sentence = input('Enter a sentence: ').upper()
different_letters: list = []
for c in sentence:
    if c not in different_letters:
        different_letters.append(c)
print(different_letters)
