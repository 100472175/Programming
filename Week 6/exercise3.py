""""
Exercise 3
@Author : Eduardo Alarcón
@version: 1.0
Date : 14-10-21
"""
import random

num = 0
total = 0
# Asks the user to enter the length of the float list to create. It must check that the number is greater than 0, if
# not, it will continue asking for the length.
while num <= 0:
    num = int(input('Please enter the length of the list: '))
list_floats = []
# Fills the list randomly with numbers between 1 and 49.
for i in range(num):
    list_floats.append(random.uniform(1.00, 49.00))
# Creates a variable called total,it will store the addition of the integer part of all the elements of the list.
for i in range(len(list_floats)):
    total += int(list_floats[i])
# Prints the list and the value of total
print(list_floats)
print(total)
