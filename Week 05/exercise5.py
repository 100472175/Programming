""""
Exercise 5: Simulating ATM
@Author : Eduardo Alarcón
@version: 1.0
"""
import random
# Create a 4-digits pin number
pin = random.randrange(0, 10_000)
pin = "%04i" % pin
balance = float(random.randint(50, 5_000))
print(pin)
# Requesting the user the pin
pin_try = input('Please, enter you pin: ')
i = 1
tries = 0
if pin_try == pin:
    tries = True
while i < 3 and not tries:
    pin_try = input('The number you entered was not your pin. This is your %i attempt Please, enter the correct pin: '
                    % i)
    i += 1
    if pin == pin_try:
        tries = False

if tries:
    print('Welcome \n ------------------------ \n1- Deposit \n2- Cash withdrawal \n3- Exit')
    chosen_operation = int(input('Choose the operation, between 1, 2 and 3: '))
    options_list = ['Deposit', 'Cash withdrawal', 'Exit']
    print('Your balance is %i' % balance)
    print('You have chosen', options_list[chosen_operation-1])
    if chosen_operation == 2:
        withdrawal_request = float(input('How much money do you want to withdraw? '))
        if withdrawal_request > balance:
            print("The operation has been denied because you don't have enough balance ")
