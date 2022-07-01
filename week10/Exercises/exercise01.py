def combine_lists(list1: list, list2: list):
    """

    :param list1:
    :param list2:
    :return: resulted list
    """
    result =[]
    for i in list2:
        list1.append(i)
    combined = list1
    for i in combined:
        if i not in result:
            result.append(i)
    return result


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
print(combine_lists(list1, list2))