"""
Exercise 6
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Write a program that creates a tuple with the names of the months of the year. Then, the program will ask
the user for a number. If the number is between 1 and the maximum length of the tuple, it will show the corresponding
 month of the year. Otherwise, it will show an error message and will ask for another number. The program will run until
  the user enters a 0.
"""
months: tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December')
num = int(input('Tell me a number between 1 and %i: ' % len(months)))

while num not in range(1, len(months)):
    num = int(input('ERROR: The number entered is not valid. Please, enter a number between 1 and %i: ' % len(months)))

if num in range(1, len(months)):
    print(months[num-1])
