"""
Exercise 1
@Author : Eduardo Alarcón
@version: 1.0
@Date : 20-10-21
Instructions:
"""
import random

matrix = []
n = int(input('What is the dimension of the matrix you want? '))

for i in range(n):
    sum_of_elements = 0
    # Creating a new sublist
    matrix.append([])
    # Repeat the number of columns - 1 times generate a random number and add it to the counter sum_of_elements
    for c in range(n - 1):
        matrix[i].append(random.randint(1, 10))
        sum_of_elements += matrix[i][c]
    # Adding the sum of elements to the matrix as the last element of each matrix
    matrix[i].append(sum_of_elements)
# print(matrix)

# Getting the values for each element and creating a string that contains all of them minus the sum
for i in range(n):
    line = ""
    for e in range(0, n-1):
        line += str(matrix[i][e]) + " + "
    # Removing the last " + "
    line = line[:-2]
    # print(line)
    # Adding the "=" and the sum of the rest of elements in the matrix
    print(line + "= " + str(matrix[i][n-1]))
