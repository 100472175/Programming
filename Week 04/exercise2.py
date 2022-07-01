""""
Exercise 2: Operator precedence
@Author : Eduardo Alarcón
@version: 1.0

"""
a, b, c, d = 5, 3, 20, 20
c -= (a + 1) / b - 3 + a % b
d -= (a + 1) / (b + 3 - 4 * a) % b
print("c:", c)
print("d:", d)

# My prediction, before running the program is 20- [(5+1)/ (3 -3 +2)] = 20 - (6/2) = 20-3 = 19

# The results of the program are 19.0 and 17.428571428571427
# These results occur because the order of the operators is first, the operators in parenthesis, then the
# division, multiplication and %. Afterwards, the sum and subtraction.

