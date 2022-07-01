"""
Exercise 2: Create three functions to: (a) ask the user for a positive number in the range (1, 10), (b) generate a
random list of this number of elements and (c) to find the minimum of the list. Create a program that uses them.
@Autor: Eduardo Alarcón
"""
import random


def function_a():
    """
    Ask the user for a positive number
    :return:
    """
    num = 0
    while num <= 0:
        num = int(input('Enter a positive number in range from 1 to 10: '))

    return num


def random_list(elements: int):
    """
    Creates a list with the number of elements being the result of
    :param elements:
    :return:
    """
    list1 = []
    for i in range(elements):
        list1.append(random.random())
    return list1


def find_minimum(list1: list):
    mini = min(list1)
    return mini


print(find_minimum(random_list(function_a())))

