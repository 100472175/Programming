""""
Exercise 13: Calculator
@Author : Eduardo Alarcón
@version: 1.0
"""
num = 0
a = input('What is the first number you want to operate with? ')
while not num:
    try:
        int(a)
        num = True
    except ValueError:
        num = False
    a = input('The key pressed was not a number. Please enter a number: ')
num = 0
b = input('What is the second number you want to operate with? ')
while not num:
    try:
        int(b)
        num = True
    except ValueError:
        num = False
    b = input('The key pressed was not a number. Please enter a number: ')

a = float(a)
b = float(b)

operation = input('What operation do you want to do between the numbers? ')
if operation in '+':
    print('The result of', a, 'plus', b, 'is', a + b)
elif operation in '-':
    print('The result of', a, 'minus', b, 'is', a-b)
elif operation in '*':
    print('The result of', a, 'multiplied by', b, 'is', a * b)
elif operation in '/':
    print('The result of', a, 'divided by', b, 'is', a / b)
elif operation in '//':
    print('The result of', a, 'integer divided by', b, 'is', a // b)
elif operation in '**':
    print('The result of', a, 'to the power of', b, 'is', a ** b)
else:
    print(operation, 'is not a valid operator')
