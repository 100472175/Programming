""""
Exercise 7: PLaying Rock, paper, scissors
@Author : Eduardo Alarcón
@version: 1.0
"""
import random

n_games = 4
cpu_random = random.randint(0, 2)
cpu_selection = ['Rock', 'Paper', 'Scissors']
user_selection = ''
print('****** %i games will be played' % n_games)
while (user_selection.lower() != 'rock' and user_selection.lower() != 'paper'
       and user_selection.lower() != 'scissors'):
    user_selection = input('Rock, Paper or Scissors? ')
    user_selection.lower()


while n_games > 0:
    while (user_selection.lower() != 'rock' and user_selection.lower() != 'paper'
           and user_selection.lower() != 'scissors'):
        user_selection = input('Rock, Paper or Scissors? ')
        user_selection.lower()
    cpu_random = random.randint(0, 2)
    print('Program chooses %s' % cpu_selection[cpu_random])
    if user_selection.lower() == 'rock':
        user_selection = 0
    elif user_selection.lower() == 'paper':
        user_selection = 1
    elif user_selection.lower() == 'scissors':
        user_selection = 2

    if user_selection == 0:
        if cpu_random == 0:
            print('*****TIE*****')
        elif cpu_random == 1:
            print('Paper wraps stone. \n******CPU WINS*****')
        else:
            print('Rock crushes scissors. \n*****PLAYER WINS*****')
    elif user_selection == 1:
        if cpu_random == 0:
            print('Paper wraps stone.\n*****PLAYER WINS*****')
        elif cpu_random == 1:
            print('*****TIE*****')
        else:
            print('Scissors cut papers. \n*****PROGRAM WINS*****')
    else:
        if cpu_random == 0:
            print('Rock crushes scissors. \n*****PROGRAM WINS*****')
        if cpu_random == 1:
            print('Scissors cut papers. \n*****PLAYER WINS***** ')
        else:
            print('*****TIE*****')
    n_games -= 1
    user_selection = ''
