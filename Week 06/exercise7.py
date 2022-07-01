"""
Exercise 7
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Write a program that receives as input a positive number, which will correspond to a quantity of money,
 and calculates and prints the minimum number of notes and coins for it, as in a previous exercise. Use a tuple to store
  the different types of notes and coins that exist.
"""

b = c = 0
quantity = input('Which quantity of money do you want to convert into notes and coins? ')
div: str = ''
num: bool = False
while not num:
    try:
        float(quantity)
        num = True
    except ValueError:
        num = False
        quantity = input('The keys pressed were not a number. Please insert a number ')

types_money = 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
rem = float(quantity)

if rem > types_money[0]:
    div = div + '500€: ' + str(int(rem // types_money[0]))
    rem = (rem % types_money[0])
if rem > types_money[1]:
    div = div + '\n200€: ' + str(int(rem // types_money[1]))
    rem = rem % types_money[1]
if rem > types_money[2]:
    div = div + '\n100€: ' + str(int(rem // types_money[2]))
    rem = rem % types_money[2]
if rem > types_money[3]:
    div = div + '\n50€: ' + str(int(rem // types_money[3]))
    rem = rem % types_money[3]
if rem > types_money[4]:
    div = div + '\n20€: ' + str(int(rem // types_money[4]))
    rem = rem % types_money[4]
if rem > types_money[5]:
    div = div + '\n10€: ' + str(int(rem // types_money[5]))
    rem = rem % types_money[5]
if rem > types_money[6]:
    div = div + '\n5€: ' + str(int(rem // types_money[6]))
    rem = rem % types_money[6]
if rem > types_money[7]:
    div = div + '\n2€: ' + str(int(rem // types_money[7]))
    rem = rem % types_money[7]
print(rem)
if rem > types_money[8]:
    div = div + '\n1€: ' + str(int(rem // types_money[8]))
    rem = rem % types_money[8]
if rem > types_money[9]:
    div = div + '\n0.50€: ' + str(int(rem // types_money[9]))
    rem = rem % types_money[9]
if rem > types_money[10]:
    div = div + '\n0.20€: ' + str(int(rem // types_money[10]))
    rem = rem % types_money[10]
if rem > types_money[11]:
    div = div + '\n0.10€: ' + str(int(rem // types_money[11]))
    rem = rem % types_money[11]
if rem > types_money[12]:
    div = div + '\n0.05€: ' + str(int(rem // types_money[12]))
    rem = rem % types_money[12]
if rem > types_money[13]:
    div = div + '\n0.02€: ' + str(int(rem // types_money[13]))
    rem = rem % types_money[13]
if rem > types_money[14]:
    div = div + '\n0.01€: ' + str(int(rem // types_money[14]))
    rem = rem % types_money[14]

print(div)
