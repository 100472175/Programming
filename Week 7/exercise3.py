"""
Exercise 3
@Author : Eduardo Alarcón
@version: 1.0
@Date : 21-10-21
Instructions: Fill a 3x3 matrix with random numbers considering that the values cannot be repeated.
Put in order the previous matrix as in the example shown below without using max(), min(), neither sort()
"""
import random

matrix = []
matrix_extended = []
matrix_sorted = []
rows = 3
columns = 3
min = 0
max = 50
counter = 0

for i in range(rows):
    matrix.append([])
    for c in range(columns):
        num = random.randint(min, max)
        while num in matrix_extended:
            num = random.randint(min, max)
        matrix[i].append(num)
        matrix_extended.append(num)

for i in range(len(matrix_extended)):
    for j in range(i + 1, len(matrix_extended)):
        if matrix_extended[i] > matrix_extended[j]:
            matrix_extended[i], matrix_extended[j] = matrix_extended[j], matrix_extended[i]

print(matrix)  # Matrix with random numbers in rows and columns
print(matrix_extended)  # Matrix with the numbers in a straight line / row

for i in range(rows):
    matrix_sorted.append([])  # Adding sub-lists for each row


for element in matrix_extended:
    if counter <= 2:  # If less than 3 elements have been added to the 1st sub-list, keep adding an element to the
        # sublist
        matrix_sorted[0].append(element)
    elif 5 >= counter > 2:
        matrix_sorted[1].append(element)
    elif counter > 5:
        matrix_sorted[2].append(element)
    counter += 1

print(matrix_sorted)
