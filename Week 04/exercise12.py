""""
Exercise 12: minimum notes and coins
@Author : Eduardo Alarcón
@version: 1.0
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

# dictio = {'ramon': 5, 'juanes': [1, b, c, 3], 'edu': 2}

rem = float(quantity)
if rem > 500:
    div = div + '500€: ' + str(int(rem // 500))
    rem = (rem % 500)
if rem > 200:
    div = div + '\n200€: ' + str(int(rem // 200))
    rem = rem % 200
if rem > 100:
    div = div + '\n100€: ' + str(int(rem // 100))
    rem = rem % 100
if rem > 50:
    div = div + '\n50€: ' + str(int(rem // 50))
    rem = rem % 50
if rem > 20:
    div = div + '\n20€: ' + str(int(rem // 20))
    rem = rem % 20
if rem > 10:
    div = div + '\n10€: ' + str(int(rem // 10))
    rem = rem % 10
if rem > 5:
    div = div + '\n5€: ' + str(int(rem // 5))
    rem = rem % 5
if rem > 2:
    div = div + '\n2€: ' + str(int(rem // 2))
    rem = rem % 2
print(rem)
if rem > 1:
    div = div + '\n1€: ' + str(int(rem // 1))
    rem = rem % 1
if rem > 0.5:
    div = div + '\n0.50€: ' + str(int(rem // 0.5))
    rem = rem % 0.5
if rem > 0.2:
    div = div + '\n0.20€: ' + str(int(rem // 0.2))
    rem = rem % 0.2
if rem > 0.1:
    div = div + '\n0.10€: ' + str(int(rem // 0.1))
    rem = rem % 0.1
if rem > 0.05:
    div = div + '\n0.05€: ' + str(int(rem // 0.05))
    rem = rem % 0.05
if rem > 0.02:
    div = div + '\n0.02€: ' + str(int(rem // 0.02))
    rem = rem % 0.02
if rem > 0.01:
    div = div + '\n0.01€: ' + str(int(rem // 0.01))
    rem = rem % 0.01

print(div)
# print("500€:", quantity // 500,'\n200€:',((quantity % 500)//200))
