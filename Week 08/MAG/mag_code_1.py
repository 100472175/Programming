def maximum(num1: int, num2: int) -> int:
    """This functions prints the maximum of 2 numbers
    @param num1 an integer number
    @param num2 other integer number
    prints as a side effect
    """
    if type(num1) == int and type(num2) == int:
        if num1 > num2:
            print('It was the first')
            return num1
        else:
            print('It was the second number or they were equal')
            return num2
    else:
        print('This function only works with integers!')


maximum(3, 7)
