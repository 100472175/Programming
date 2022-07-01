""""
Exercise 6: Cinema ticket according to age
Author : Eduardo Alarcón
@version: 1.0
"""
age = int(input('What is the age of the customer? '))
price = 9
if age < 5:
    print('The price for the ticket if the customer has %i years is %.2f €' % (age, float(price * 0.4)))
elif age > 60:
    print('The price for the ticket if the customer has %i years is %.2f €' % (age, float(price * 0.45)))
elif age < 26:
    print('The price for the ticket if the customer has %i years is %.2f €' % (age, float(price * 0.8)))
else:
    print('The price for the ticket if the customer has %i years is %i €, which is the normal price'
          % (age, price))
