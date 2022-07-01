""""
Exercise 8: Is this a number?
@Author : Eduardo Alarcón
@version: 1.0
"""
numbers = '1234567890'
works = True
var1 = input('Press a key on the keyboard: ')
# This only works for one number
if var1 in numbers:
    print('The key pressed is a number')
else:
    print('The key pressed is not a number')
# This works for multiple characters
for c in var1:  # For every character in the variable 1
    if c not in numbers:  # For every character not in the string numbers
       works = False  # The keys entered were not a number
    else:
        works = True
if works:
    print("Funciona")
else:
    print("No funciona")

