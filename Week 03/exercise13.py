a: float = 1e300
b: float = 1e300
# If we try to put 2e308 as a float, python will consider it as infinity and any operation
# will result in infinity
print(a,b)
c = a * b
float(c)
print(c)
# The result from multiplying a and b will be infinity

d = a ** b
print(d)
# The result of doing this operation is OverflowError
