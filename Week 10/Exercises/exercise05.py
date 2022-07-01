"""
Create a program that creates functions which are your own versions of the list methods. Do not make use of any
built-in list methods to implement them. Your program must do all the necessary checks to make sure that all the
functions work. For functions modifying the original list, the list must no be changed, but a modified version of
 it must be returned.
count(list1, x): returns the number of elements with the specified value.
index(list1, x): returns the index of the first element with the specified value. If the value
does not exist, the function returns None.
append(list1, x): adds an element at the end of the list.
insert(list1, x, index): adds an element at the specified position. remove(list1, x): removes the first element in
the list with the specified value. removeAll(list1, x): removes all the elements in the list with the specified value.
 clear(list1): removes all the elements from the list.
pop(list1): removes the last element of the list and returns its value.
"""


def count_f(list1: list, num: int) -> int:
    """

    :param list1:
    :param num:
    :return:
    """
    list2 = list1
    counts = 0
    for i in range(len(list1)):
        if list2[i - 1] == num:
            counts += 1

    return counts


def index_f(list1: list, num: int):
    for i in range(len(list1)):
        if list1[i - 1] == num:
            return i - 1


def append_f(list1: list, num: int):
    list2 = list1
    list2 += num
    return list2


def insert_f(list1: list, num: int, position: int):
    list2 = list1
    list2 = list2[:position]
    list2 += num
    for i in range(len(list1) - position):
        i += position
        list2 += list1[i]
    return list2


def insert_f(list1: list, num: int):
    removed = False
    list2 = list1
    position = 0
    while not removed:
        for i in list1:
            if list1[i-1] == num:
                position = i-1
                removed = True
    for i in range(len(list2)-position):
        i += position
        list2[i] = list1[i-1]
    return list2

list1 = [3, 4, 5, 6, 7, 3, 2, 4, 3, 2, 2]
list1.remove(9)



