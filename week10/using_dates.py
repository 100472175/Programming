# This allows us to use the Date class form the dates file into this program
from dates import Date

# In this case, var1 is an object
# Assigning the "type" is mandatory
var1 = Date()
print(type(var1))
var1.day = 28
var1.month = 'July'
var1.year = 2022
var1.leap_year = False
print(var1.day)
var2 = Date()
var2.day = 12
var2.month = 'October'
var3 = Date()
var3.pepe = 'test'
print(var3.pepe)
var5 = Date()
# Do not assign an object to another one, they are only pointers.
var5.month = 'March'
print(var1.month)

