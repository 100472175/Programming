""""
Exercise 1
@Author : Eduardo Alarcón
@version: 1.0
Date : 14-10-21
"""
# Generating a list with 5 elements
list1 = [1, 23, 4, 5, 'hello']
# Assigning the element of the list 1 to the element 2
list1[2] = list1[1]
print(list1)
print(list1[2])
print(list1[1])
list1[2] = 'the world ends with you'
print(list1[2])
print(list1[1])
# No, the first element doesn't change when changing the other element as they are a copy from each other, not a
# reference to a place in memory. The same would happen if we changed the first element

