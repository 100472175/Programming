""""
Exercise 5: two name
@Author : Eduardo Alarcón
@version: 1.0
"""
print('Please enter the names and ages of the people you want to compare using the next format : "name age" ')
a = input('Please enter the first name and age: ')
b = input('Please enter the second name and age: ')

# print(a[-2:])
if int(a[-2:]) > int(b[-2:]):
    print(a[:-3], 'is older than', b[:-2])
if int(b[-2:]) > int(a[-2:]):
    print(b[:-3], 'is older than', a[:-2])
if int(b[-2:]) == int(a[-2:]):
    print(a[:-3], 'and', b[:-3], 'are the same age')
