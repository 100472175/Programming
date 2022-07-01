"""
Exercise 4
@Author : Eduardo Alarcón
@version: 1.0
@Date : 21-10-21
Instructions:  wood workshop sells wood boards of 10 different sizes, which they call size 0, size 1, etc.
Create a program that:
a. Generates 10 random numbers, between 0 and 10. Each one will represent the stock for each available board size.
    It must print the number of boards of each size in the warehouse.
b. Asks the user about the number of customers that will buy boards. It will keep asking while it is smaller than 1.
c. Automatically generates an order for each of the customers. Each order will contain for each available size a random
    number of boards between 0 and 4.
d. Prints the orders into the screen.
e. Sells boards to the customers, starting by the first one, reducing the number of boards in the stock.
f. Prints the pending orders for each customer (only if he/she has pending orders). A pending order is the number of
   boards of each size that cannot be sold as there are not enough boards in stock.
"""
import random
num_customers = 0
customer_order = []

stock = {}
for i in range(0, 10):
    stock['size' + str(i)] = random.randint(0, 10)
while num_customers <= 1:
    num_customers = int(input('How many customers do you have? '))

for c in range(num_customers):
    customer_order.append([])
    for e in range(len(stock)):
        customer_order[c].append(random.randint(0, 4))
    # print(customer_order[c])


print(*stock, sep='\t', end='         Stock\n')
print(*stock.values(), sep='\t\t')
print('Customer orders: ' + str(num_customers))
for i in range(len(customer_order)):
    print(*customer_order[i], sep='\t\t', end='             Customer %i\n' % (i+1))
"""
for d in range(len(stock)):
    for i in range(len(customer_order)):
        for s in stock.keys():
            if stock[s] > customer_order[i][d]:
                aux = stock[s]
                customer_order[i][d] -= stock['size0']
"""

for i in range(num_customers):
    if stock['size0'] >= customer_order[i][0]:
        a = stock['size0']
        stock['size0'] -= customer_order[i][0]
        customer_order[i][0] = 0
    if stock['size1'] >= customer_order[i][1]:
        a = stock['size1']
        stock['size1'] -= customer_order[i][1]
        customer_order[i][1] = 0
    if stock['size2'] >= customer_order[i][2]:
        a = stock['size2']
        stock['size2'] -= customer_order[i][2]
        customer_order[i][2] = 0
    if stock['size3'] >= customer_order[i][3]:
        a = stock['size3']
        stock['size3'] -= customer_order[i][3]
        customer_order[i][3] = 0
    if stock['size4'] >= customer_order[i][4]:
        a = stock['size4']
        stock['size4'] -= customer_order[i][4]
        customer_order[i][4] = 0
    if stock['size5'] >= customer_order[i][5]:
        a = stock['size5']
        stock['size5'] -= customer_order[i][5]
        customer_order[i][5] = 0
    if stock['size6'] >= customer_order[i][6]:
        a = stock['size6']
        stock['size6'] -= customer_order[i][6]
        customer_order[i][6] = 0
    if stock['size7'] >= customer_order[i][7]:
        a = stock['size7']
        stock['size7'] -= customer_order[i][7]
        customer_order[i][7] = 0
    if stock['size8'] >= customer_order[i][8]:
        a = stock['size8']
        stock['size8'] -= customer_order[i][8]
        customer_order[i][8] = 0
    if stock['size9'] >= customer_order[i][9]:
        a = stock['size9']
        stock['size9'] -= customer_order[i][9]
        customer_order[i][9] = 0




print("\n Pending Orders:")
for i in range(len(customer_order)):
    print(*customer_order[i], sep='\t\t', end='             Customer %i\n' % (i+1))
