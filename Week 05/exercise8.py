""""
Exercise 8: Simplified version of BlackJack
@Author : Eduardo Alarcón
@version: 1.0
"""
import random

game_number = -1 * int(input('How many games do you want to play? '))
game_count = 0
dice, dice_2 = 0, 0
accumulated_A, accumulated_B = 0, 0
replay: bool = True
results = False

while game_number < 0:
    # Resetting all variables to play a game
    dice, dice_2 = 0, 0
    accumulated_A, accumulated_B = 0, 0
    replay = True
    results = False
    # PLayer 1
    game_count += 1
    print('GAME %i - PLAYER 1' % game_count)
    while replay:
        # roll_dice_A()
        dice = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print('The number of points obtained are %i and %i' % (dice, dice_2))
        accumulated_A += dice
        accumulated_A += dice_2
        print('The points accumulated are %i' % accumulated_A)
        if accumulated_A < 21:
            replay: str = input('Would you like to roll the dice again? (yes/no) ')
            if replay != 'yes':
                replay = False
        else:
            replay = False
    # Player 2
    if accumulated_A > 21:
        replay = False
    else:
        replay = True
    print('GAME %i - PLAYER 2' % game_count)
    while replay:
        # roll_dice_A()
        dice = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print('The number of points obtained are %i and %i' % (dice, dice_2))
        accumulated_B += dice
        accumulated_B += dice_2
        print('The points accumulated are %i' % accumulated_B)
        if accumulated_B < 21:
            replay: str = input('Would you like to roll the dice again? (yes/no) ')
            if replay != 'yes':
                replay = False
        else:
            replay = False

    if accumulated_A > 21:
        print('*****PLAYER 2 WINS*****\n')
        replay = True
    if accumulated_B > 21:
        print('*****PLAYER 1 WINS*****\n')
        replay = True
    if accumulated_A > accumulated_B:
        print('*****PLAYER 1 WINS*****\n')
        replay = True
    elif accumulated_A < accumulated_B:
        print('*****PLAYER 2 WINS*****\n')
        replay = True
    else:
        print('*****TIE*****\n')
        replay = True
    game_number += 1
