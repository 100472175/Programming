""""
Exercise 3
@Author : Eduardo Alarcón
@version: 1.0
"""

num = int(input('Enter the number to search every lower perfect number: '))
list_result = []
addition = 0
while num >= 1:
    for i in range(1, num):
        if num % i == 0:
            addition += i
    if addition == num:
        list_result.append(num)
    addition = 0
    num -= 1
i = 0
while i < len(list_result):
    print('The number %i is perfect' % list_result[i])
    i += 1
