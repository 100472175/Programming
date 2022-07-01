"""
Exercise 4
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Write a program to create a 20 elements int list and filling it randomly with numbers in the range 1 to 9.
 Ask the user for a number between 1 and 9 (the program must check that the number is in the desired range) and print if
  the number is in the list and all the positions where it appears.
"""


import random
list1 = []
counter = 0
positions = []
num = input('Please, enter a number between 1 and 9: ')
for _ in range(20):
    list1.append(random.randint(1, 9))
while num not in '123456789':
    num = int(input('Please, enter a number between 1 and 9: '))

for e in range(1, len(list1)):
    if str(list1[e]) == num:
        counter += 1
        positions.append(e)
print(list1)
print('There are %i number of %s and it appears on positions %s' % (len(positions), num, positions))


"""
import random
list1 = []
positions = ''
num = input('Please, enter a number between 1 and 9: ')
for _ in range(20):
    list1.append(random.randint(1, 9))
while num not in '123456789':
    num = input('Please, enter a number between 1 and 9: ')

if int(num) in list1:
    list1.sort()
    a = list1.index(int(num))
    list1 = list1[a:]
    list1.reverse()
    b = list1.index(int(num))
    list1 = list1[b:]
    positions = [a]
    positions.clear()
    for i in range(len(list1)):
        positions.append(a+i)
    print('There are %i number of %s and it appears on positions %s' % (len(list1), num, positions))
else:
    print('The number is not in the list')
"""