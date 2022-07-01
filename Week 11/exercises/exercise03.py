"""
Create a Dice class with fields name and rolls, to simulate a dice game. The rolls field must be a list. Create an init
 method that receives the name of the player and an integer n, which represents the number of rolls. It must assign the
  name to the corresponding field and create a list of n elements randomly filled with numbers from 1 to 6. Create a
  two-player game asking each player his/her name. It must print the results for each one and calculate the winner,
   which will be the one with the highest number of equal dice. In case of a tie, the one with the highest total score
   will win.

"""
import random


class Dice():
    def __init__(self, name1: str, name2: str, number_of_rolls: int):
        self.name1 = name1
        self.name2 = name2
        self.rolls2 = []
        self.rolls1 = []
        self.results = []
        self.number_of_rolls = number_of_rolls
        for i in range(number_of_rolls):
            self.rolls1.append(random.randint(1, 6))
            self.rolls2.append(random.randint(1, 6))
            if self.rolls1[i] == self.rolls2[i]:
                self.results.append(0)
            elif self.rolls1[i] >= self.rolls2[i]:
                self.results.append(1)
            else:
                self.results.append(-1)

        def __str__(self):
            return str(self.rolls1) + '\n ' + str(self.rolls2)


player1_n = input('What is your name? ')
player2_n = input('What is your name? ')
num_of_rows = int(input("How many rools do you want? "))

player1 = Dice(player1_n, player2_n, num_of_rows)

print(player1)
