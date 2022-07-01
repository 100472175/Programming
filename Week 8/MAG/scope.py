import random
a = 8


def a_function(param1: int, param2=random.random(), param3=a) -> float:
    result = param1 + param2 + param3
    return result


def another_function(param1: int, param2=random.random()) -> float:
    result = param1 - param2
    return result
