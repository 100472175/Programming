"""
Functions II

append(list1, x): adds an element at the end of the list.
insert(list1, x, index): adds an element at the specified position. remove(list1, x): removes the first element in
  the list with the specified value. removeAll(list1, x): removes all the elements in the list with the specified value.
clear(list1): removes all the elements from the list.
pop(list1): removes the last element of the list and returns its value.
"""


def f_append(list1, element):
    list1 += []
    list1[-1] = element





def my_function(arg):
    print("list received {} has id {}". format(arg, id(arg)))
    arg. append(40)
    print("list changed {} has id {}". format(arg, id(arg)))



x = [10, 20, 30]
print("list sent {} has id {}". format(x, id(x)))
my_function(x)
print("list after function call {} has id {}". format(x, id(x)))

