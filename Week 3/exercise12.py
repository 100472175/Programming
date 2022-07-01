name = 'Johnny Depp'
age = 55
height = 1.78
weight = 65.4
eyes = 'brown'
hair = 'brown'
# S will be a striong, an i will be an integer, an f will be a float, and we can specify how
# many decimals we want, for example %.2f will give us 2 decimals

print("Let’s talk about %s." %name)
print("He's %i years old" %age)
print("He’s %.2f meters tall." %height)
print("He’s %.6f kilograms heavy." %weight)
print("Actually that’s not too heavy.")
print("He has %s eyes and %s hair." % (eyes, hair))

# I have rewritten the program to add the variables inside the strings.
print("Let’s talk about", name)
print("He's", age, "years old")
print("He’s", height, "f meters tall.")
print("He’s", weight, "kilograms heavy.")
print("Actually that’s not too heavy.")
print("He has ", eyes, " eyes and ", hair, " hair.")
