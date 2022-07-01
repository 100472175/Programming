def multiply_by_2(parameter: int) -> int:
    parameter *= 2
    return parameter


def multiply_list_by_2(param: list):
    for i in range(len(param)):
        param[i] *= 2
        # Without using the return, we change the list itself
    # return param
