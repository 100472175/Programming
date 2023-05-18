"""
Exercise 6
@Author : Eduardo Alarcón
@version: 1.0
@Date : 21-10-21
Instructions: Given the following dictionary, Add a key to toyShop called ’fluffyToy’ and set its value as a list
 consisting of the strings ’bear’, ’dog’, and ’cat’. Remove ’Batman’ from the list of items stored under the ’puzzles’
 key. Add 100 to the number stored under ’dolls’ key.
"""
toyShop = {
    'dolls': 500,
    'games': ['Guess who?', 'Clue', 'Battleship'],
    'puzzles': ['Star Wars', 'Batman', 'Ironman'],
}

toyShop['fluffyToy'] = ['bear', 'dog', 'cat']
del(toyShop['puzzles'][0])
print(toyShop['puzzles'])
toyShop['puzzles'].remove('Batman')

print(toyShop['puzzles'])
toyShop['dolls'] += 100

print(toyShop)

