"""
fibonacci
"""


def fibonacci(num: int) -> list:
    fib_list = []
    fib_list.append(0)
    if num > 1:
        fib_list.append(1)
        for i in range(num - 1):
            fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
    return fib_list


a = int(input('How many elements, exluding the 0 do you want from the fibonacci sequence? '))
print(fibonacci(a))
