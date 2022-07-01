"""
Exercise 2
@Author : Eduardo Alarcón
@version: 1.0
@Date : 20-10-21
Instructions: Create a program to generate two matrices (as lists of lists) of integers M1 and M2, which can be of
 different size, by requesting the sizes and the values by keyboard. Then it should show the elements of M1 that are
  included on M2.
"""
column1 = int(input('Specify the number of rows of the M1 matrix and press Enter: '))
row1 = int(input('Specify the number of columns of the M1 matrix and press Enter: '))


m1 = []
m1_extended = []
# Creates a list with n elements, which will be rows
for i in range(column1):
    m1.append([])
    # In each row, we create n elements, to create the columns
    for o in range(row1):
        user = int(input('Introduce the term in the %i , %i position and press Enter: ' % (i+1, o+1)))
        # Filling the matrix with the elements provided by the user, going one at a time
        m1[i].append(user)
        m1_extended.append(user)

print('The M1 matrix is: ')
for i in range(column1):
    line = ""
    for _ in range(row1):
        line += str(m1[i][_]) + ' '
    print(line)

# Ask the user for the number of columns and rows of the second matrix
column2 = int(input('Specify the number of rows of the M2 matrix and press Enter: '))
row2 = int(input('Specify the number of columns of the M2 matrix and press Enter: '))

m2 = []
m2_extended = []
for i in range(column2):
    m2.append([])
    for o in range(row2):
        user = int(input('Introduce the term in the %i , %i position and press Enter: ' % (i + 1, o + 1)))
        m2[i].append(user)
        m2_extended.append(user)

print('The M2 matrix is: ')
for i in range(column2):
    line = ""
    for _ in range(row2):
        line += str(m2[i][_]) + ' '
    print(line)

coincided = ''
for k in range(len(m1)):  # Get all rows of the 1st matrix
    for j in m1[k]:  # Get all the elements of all rows of the 1st matrix
        for l in range(len(m2)):  # Get all rows of the 2nd matrix
            for n in m2[l]:  # Get all elements od the rows of matrix 2
                if j == n:
                    if str(j) not in coincided:
                        print('The term ' + str(j) + ' is included in both matrices')
                        coincided += str(j)




