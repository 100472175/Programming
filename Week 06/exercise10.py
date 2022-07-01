"""
Exercise 10
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Filling lists
"""
import random
import time

start = time.time()
list1 = []
for i in range(100_000):
    list1.append(random.randint(1, 100))
end = time.time()
print('The time it took to fill the list with .append is %.10f' % (end-start))

start2 = time.time()
list2 = []
for i in range(100_000):
    list2 += [random.randint(1, 100)]
end2 = time.time()
print('The time it took to fill the list with the += operator is %.10f' % (end2-start2))

start3 = time.time()
list3 = []
for i in range(100_000):
    list3 = list3 + [random.randint(1, 100)]
end3 = time.time()
print('The time it took to fill the list with the " list3 = list3 + random_number operator is %.10f' % (end3-start3))

