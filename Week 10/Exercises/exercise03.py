"""
Create a function that receives as parameters a list and an element and returns a tuple with the positions of the
element in the list, or the empty tuple if the element is not in the list. Invoking this function, create another
one that receives two lists and an element and returns if any of the appearances of the element is at the same
position in both lists.
"""


def functs (list1: list, num: int):
    """
    
    :param list1: 
    :param num: 
    :return: a tupple, possition of the list of the element, or empty
    """
    position = None
    if num in list1:
        position = (list1.index(num))

    return position


def two_lists(list1: list, list2: list, num: int):
    pos_1, pos_2 = None, None
    if num in list1:
        pos_1 = list1.index(num)
    if num in list2:
        pos_2 = list2.index(num)
    if pos_1 == pos_2:
        return 'The element is in both lists'


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element = int(input('What element do you want to know the position from the list? '))
position = functs(list1, element)
print('The position of', element, 'is', position,'in this list:', list1)