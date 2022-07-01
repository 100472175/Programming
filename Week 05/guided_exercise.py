"""
Guided Exercise 3
@Author: Eduardo Alarcón
@version : 1.0
"""
import random

rest = 0
soldiers: int = int(input("What are the number of soldiers on our side? "))
engines: int = int(input("What is the number of siege engines? "))
# Warning: any non-empty string will be True, even the str 'False'
poison: bool = bool(input("Are we going to use poison? (Press enter for No) "))
wood = 0

satisfied = False
if (soldiers >= 500
        and engines >= 50):
    print('The best strategy is A: "Silent attack".')
    satisfied = True
if soldiers > 10_000:
    print('The best strategy is B: "Crossfire".')
    satisfied = True
if (soldiers >= 1
        and poison):
    print('The best strategy is C: "Kill the king".')
    satisfied = True

if not satisfied:
    print("None of the three strategies is satisfied completely. I'll choose 1 randomly and try to buy re remaining"
          "elements needed for the attack:")

    mine = random.randint(1, 3)
    if mine == 1:
        # Requirements for strategy A
        mine = [500, 50, 0]
    elif mine == 2:
        # Requirements for strategy B
    mine = [10000, 0, 0]
    else:
            # Requirements for strategy C
        mine = [1, 0, True]

    coins = int(input("What is the number of budget you have at your disposal?"))
    rest_coins = coins
    # Resources at our disposal
    list0 = [soldiers, engines, poison]
# Comparing the soldiers and buy them if necessary
    if list0[0] < mine[0]:
        rest = list0[0] - mine[0]
        if rest * 10 < rest_coins:
            rest_coins -= rest * 10
            print('1 soldier was bought. 10 golden budget were used. (%i times)', rest)
            wood = 10 * rest
            rest = 0

# Comparing the siege machines and buy them if necessary
    if list0[1] < mine[1]:
        rest = list0[1] - mine[1]
        rest_wood = wood
        if 5 * rest < rest_coins:
            rest_coins -= 5 * rest
            if wood < 200 * rest:
                rest_wood -= 200 * rest
            elif 2 * rest_coins > rest_wood:
                rest_coins -= rest_wood / 2

'''
1 soldier = 10 budget
1 siege  = 200 wood, 50 iron
1 poison = 100 wood, 50 herbs, 100  budget


20 wood = 10  budget
10 herbs= 10  budget
5 iron = 10  budget
for each soldier, 10 wood recieved
'''
