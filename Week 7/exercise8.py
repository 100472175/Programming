"""
Exercise 1
@Author : Eduardo Alarcón
@version: 1.0
@Date : 20-10-21
Instructions: Create a dictionary with keys the names of the months of the year and values the number of days of that
 month (‘January’: 31, etc). Create another dictionary with keys: day, month, year and leapYear. Ask the user to fill
  the second dictionary. The value of leap year must be automatically set. The value of the month and day must be
  correct taking into account leap years (those years February has 29 days). If any value is not correct we will ask
   the user until a correct value is entered. Print the date with format: March 23, 2019, non-leap year
"""
months_dict = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
               'September': 30, 'October': 31, 'November': 30, 'December': 31}
dict2 = {'day': None, 'month': None, 'year': None, 'leapYear': None}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

day = int(input('What day of the month is it? '))
dict2['day'] = day

dict2['month'] = input('What month is it? ')
dict2['year'] = int(input('What year is it? '))

if dict2['year'] % 4 == 0:
    if dict2['year'] % 100 == 0:
        if dict2['year'] % 400 == 0:
            dict2['leapYear'] = 'Leap Year'
        else:
            dict2['leapYear'] = 'Non leap year'
    else:
        dict2['leapYear'] = 'Leap year'
else:
    dict2['leapYear'] = 'Non leap year'

print(dict2['month'] + ', ' + str(dict2['day']) + ', ' + str(dict2['year']) + ', ' + str(dict2['leapYear']))
