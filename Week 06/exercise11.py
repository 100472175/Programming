"""
Exercise 11
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Create a list of 100 integer numbers in the range 1 to 1000 and print it. Next remove from it all the even
 numbers and print it again.
"""
import random

list1 = []
for i in range(100):
    list1.append(random.randint(1, 1_000))
print(list1)
for e in range(0, 1_000, 2):
    while e in list1:
        list1.remove(e)

print(list1)
