""""
Exercise 2
@Author : Eduardo Alarcón
@version: 1.0
"""
import random
# Asking th user to input 2 numbers
print('The numbers you have to enter must check this statement: "a+5 < b"')
a = b = 0

'''a = int(input('Please, enter the first number: '))
b = int(input('Please, enter the second number: '))
# Creating a list with the users election of numbers
user_list = [a, b]'''

# Checking if the numbers the user entered were valid
while not a+5 < b:
    a = int(input('Please, enter the first number: '))
    b = int(input('Please, enter the second number: '))
    print('The numbers entered were not acceptable')
user_list = [a, b]
# Generating 5 random numbers and assigning them to 5 variables
num1 = random.randint(a, b)
num2 = random.randint(a, b)
num3 = random.randint(a, b)
num4 = random.randint(a, b)
num5 = random.randint(a, b)
# Seeing if the numbers generated randomly are even
while num1 % 2 != 0:
    num1 = random.randint(a, b)

while num3 % 2 != 0:
    num3 = random.randint(a, b)

while num5 % 2 != 0:
    num5 = random.randint(a, b)
# Checking if the numbers generated randomly are odd
while num2 % 2 == 0:
    num2 = random.randint(a, b)

while num4 % 2 == 0:
    num4 = random.randint(a, b)
# Creating a list of all random numbers to easily print them
random_list = [num1, num2, num3, num4, num5]

# print("For the interval [", a, ",", b, "] a valid sequence of numbers is", random_list)
print("For the interval", user_list, "a valid sequence of numbers is", random_list)
