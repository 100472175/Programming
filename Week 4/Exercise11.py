""""
Exercise 11: Leap years
@Author : Eduardo Alarcón
@version: 1.0
"""

year = input('What is the year you want to check if it is a leap-year? ')
num = False

while not num:
    try:
        int(year)
        num = True
    except ValueError:
        year = input('What is the year you want to check if it is a leap-year? ')
year = int(year)

if year < 2021:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('The year', year, 'was a leap-year')
            else:
                print('The year', year, 'was not a leap-year')
        else:
            print('The year', year, 'was a leap-year')
    else:
        print('The year', year, 'was not a leap-year')
else:
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 == 0:
                print('The year', year, 'will be leap-year')
            else:
                print('The year', year, 'will not be leap-year')
        else:
            print('The year', year, 'will not be leap-year')
    else:
        print('The year', year, 'will not be leap-year')
