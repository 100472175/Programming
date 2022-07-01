variable1: float = 12345678901234567.0
variable2: float = 12345678901234568.0
print(variable1-variable2)  # The result of this print is 0.0 because only the first 16decimal points are stored
# Now, lets try with 2 variables that are integers
variable3: int = 12345678901234567
variable4: int = 12345678901234568
# The resilt is -1 because integers can be as big as the memory allows
print(variable3-variable4)  # The result of this operation is -1
print(0.3-0.2)  # The result of this operation is 0.0999999999999999998
