""""
Exercise 4
@Author : Eduardo Alarcón
@version: 1.0
"""
works = 0
num = 0
while not works:
    num = input('Enter the characters you want to check if there are a number: ')
    if num.isdigit():
        works = 1
    else:
        num = round(float(num))
        num = int(num)
print('The characters are a number. And the square of the number entered is', int(num)**2)

num = input("")
while not num.replace('.','',1).isdigit(): # Remplaza el caracter "." por nada ('') y cuantas veces quieres que lo haga
    num = input()
print(float(num)**(1/2))

while True:
    try:
        print(float(num)**(1/2))
        break
    except ValueError:
        num = input()

