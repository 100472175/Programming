""""
Exercise 9: Coordinates on a plane
@Author : Eduardo Alarcón
@version: 1.0
"""
x: int = int(input('Enter the first coordinate, on the x plane: '))
while x == 0:
    x = int(input('Please reenter the x coordinate '))

y: int = int(input('Enter the second coordinate, on the y plane: '))
while y == 0:
    y = int(input('Please reenter the y coordinate '))

if x > 0:
    if y > 0:
        print('The coordinates are in the 1st quadrant')
    else:
        print('The coordinates are in the 4th quadrant')
else:
    if y > 0:
        print('The coordinates are in the 2nd quadrant')
    else:
        print('The coordinates are in the 3rd quadrant')




