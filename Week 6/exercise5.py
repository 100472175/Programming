""""
Exercise 5
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Write a program that guesses the number that the user has thought (1 to 100). The program will generate
 random numbers and must control that none of them is repeated. It will also be able to detect if the user is lying
 (if it has already tried all the numbers and the user says it is none of them). It has also to count how many attempts
  were needed to guess the number.
"""
import random
guessed = False
works = 0
attempts = 0
used_list = []
used_list.clear()
rng = 0
minimum = 1
maximum = 100
while not works:
    rng = random.randint(minimum, maximum)
    cheated_counter = 0
    while rng in used_list:
        rng = random.randint(minimum, maximum)
        cheated_counter += 1
        if cheated_counter == 100:
            print('You have cheated. I went through all numbers between %i and %i' %(minimum, maximum))
    works = input('Is your number %i? ' % rng)
    if works.lower() in 'yes':
        guessed = True
    elif works.lower() in 'no':
        guessed = False
        works = False
    used_list.append(rng)
    attempts += 1
if guessed:
    print('I have guessed your number, which is %i and it took me %i attempts' % (rng, attempts))