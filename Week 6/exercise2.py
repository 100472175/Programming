""""
Exercise 2
@Author : Eduardo Alarcón
@version: 1.0
Date : 14-10-21
"""
import copy
import random

list1 = []
for i in range(25):
    list1.append(random.randint(0, 1000))
list2 = list1
print(list1)
print(list2)
list1[1] = "We can fly, unbreakable"
print(list1)
print(list2)
# As we can see, the second list changes because we are assigning a "second name" to the same place in memory so when
# changing one, the other one, which is the same, it also changes.
list3 = []
for i in range(35):
    list3.append(random.randint(-999, 0))
list4 = copy.deepcopy(list3)
list3[3] = '“No matter what lies you tell, you can’t fool your own heart.”'
print(list3)
print(list4)
# When we copy the list with the deepcopy, we are copying all the elements, not the pointers
