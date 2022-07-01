""""
Exercise 6:
@Author : Eduardo Alarcón
@version: 1.0
"""
# Create a list, order it, get the fist, the lass, all the additions, to do the average and finish when negative input
grade = 0
grades_list = []
addition = 0
average = 0
while grade >= 0:
    grade = float(input('Enter a grade from a student: '))
    addition = 0
    if grade < 0:
        break
    grades_list.append(grade)
    grades_list.sort()
    grades_list.reverse()
    for i in grades_list:
        addition = addition + i
    length = len(grades_list)
    average = addition / length
    print('The highest mark is %.2f, the lowest mark is %.2f. The average of the grades is %.2f and the number of '
          'students that have taken the course is %i' % (grades_list[0], grades_list[-1], average, length))
