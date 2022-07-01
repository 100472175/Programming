import random


def createListNumbers():
    list1 = []
    for i in range(10):
        list1.append(random.randrange(0, 10000000000000, 2))
    return list1


def calculateFigures(list1: list):
    """

    :param list1: list to get max and min
    :return: maximum and minimum
    """
    maxi = max(list1)
    mini = min(list1)
    return maxi, mini


list_final = createListNumbers()
print('The list is: ', list_final )
print('These are the maximum and minimum of the list: ', calculateFigures(list_final))


