"""
Define a function that returns a tuple simulating the behaviour of the function range(start,stop,step), which returns
 a sequence of numbers between the given start integer to the stop integer incremented by the given step integer.
 Configure the function with optional parameters so it also works to simulate functions range(start, stop) and
 range(stop). You must check that the types of the parameters are correct (int) and that their range is also correct.
 If not an empty tuple will be returned.
"""


def range_custom(stop: int, start=1, increase=1):
    """

    :param stop:
    :param start:
    :param increase:
    :return:
    """
    list_num = ()
    count = 1
    correct = None
    if type(stop) == int and type(start) == int and type(increase) == int:
        correct = True
    if not correct:
        list_num = []
        while count <= int(stop):
            list_num.append(count)
            count += increase

    return list_num


a_sel, b_sel, c_sel, ranges = False, False, False, None

a = int(input('Enter the values you want to execute in a tupple with this format: '))
if a != '':
    a_sel = True

b = input('Enter the start of your range, press ENTER to skip: ')
if b != '':
    b_sel = True
c = input('Enter the interval or your range, press ENTER to skip: ')
if c == '':
    c_sel = True

if a_sel and b_sel:
    ranges = range_custom(a, b)
if a_sel and c_sel:
    ranges = range_custom(a, c)
if a_sel and b_sel and c_sel:
    ranges = range_custom(a, b, c)

print(ranges)
