""""
Exercise 1
@Author : Eduardo Alarcón
@version: 1.0
"""
# We need to import the library random to use the random function
import random

# These variables are the number of tries the user has tries to guess the number,
# the second one is the number going to be checked against
# and the last one is the random number
tries = 0
hidden = random.randint(1, 20)

intent = int(input('Please, make your guess:'))

while intent != hidden:
    # Checking if the number the user inputted, is greater than the number randomly generated
    if intent > hidden:
        print('The number you entered is greater than the random number generated')
        # Adding one to the number of tries
        tries += 1
        # Asking again the user of another number
        intent = int(input('Please, make your guess:'))
# Checking if the number the user entered is smaller than the number randomly generated
    elif intent < hidden:
        print('The number you entered is smaller than the random number generated')
        # Adding one to the number of tries
        tries += 1
        # Asking again the user of another number
        intent = int(input('Please, make your guess:'))
# As the number has "escaped" the while loop, the number chosen is equal to the hidden one
tries += 1
print('Hurray, the number you entered is the one generated randomly, and you have guessed %i times' % tries)
