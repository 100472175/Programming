""""
Exercise 4: reading 2 integers and not dividing them if the second one is 0
@Author : Eduardo Alarcón
@version: 1.0
"""

a:int = int(input('Please enter the first number you want to divide: '))
b:int = int(input('Please, enter the number you want the first one to be divided by: '))
# Checking if the second number is 0
if b != 0:
    print(a/b)
else:
    print('Cannot divide by 0')


