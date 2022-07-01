import random
import cmath


def minmax(minimum: int, maximum: int, type_output: str):
    """
    :param minimum: Mimimum number
    :param maximum: Maximum number
    :param type_output: to indicate what needs to be returned, int, float, complex
    :return: 
    """
    if type_output == 'int':
        num = random.randint(minimum, maximum+1)
    elif type_output == 'float':
        num = random.randrange(minimum, maximum) + random.random()
    else:
        num_x = random.randrange(minimum, maximum)
        num_y = random.randrange(minimum, maximum)
        num = complex(num_x, num_y)

    return num


mini = int(input("What is the minimum number of your range: "))
maxi = int(input("What is the maximum number of your range: "))
output = input("WIn what format do you want an average value: an integer (int), a floating number (float) or a complex"
               "number (complex) ")
print("The result of the random number in the range specified is", minmax(mini, maxi, output))
