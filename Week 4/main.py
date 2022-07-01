"""
Created on Wed Sep 29 10:30 2020
@author: Eduardo Alarcón Navarro
@version: 1.1
"""
# These are the variables used in this program
time: str
number_soldiers: int
siege: int
poison: str
rain: str
yes = "YesyesYeahyeah"
no = "NonoNopnop"
a = b = c = counter = 0
satisfyA, dn_satisfyA = "", ""
satisfyB, dn_satisfyB = "", ""
satisfyC, dn_satisfyC = "", ""

# These are the prompts asking the user to input the program the
time = input("Are you attacking by day time? ")
number_soldiers = int(input("What are the number of soldiers on our side? "))
siege = int(input("What is the number of siege engines? "))
poison = input("Are we going to use poison? ")
rain = input("Is it raining? ")

# Strategy 1. The if counter checks for every condition and the and comparators, only have a result 1 when every one
# is true so, all have to be true to be executed
if counter == 0:
    if time in no and rain in yes and number_soldiers >= 500 and siege >= 50:
        print("The recommended strategy is A: “Silent attack”.")
        a = 0
    else:
        # The a variable is to check if a strategy has been already chosen
        a = 1

# Checking if Strategy 2, aka Crossfire is suitable with the parameters inputted
if counter == 0:
    if time in yes and number_soldiers >= 10_000:
        print("The recommended strategy is B: “Crossfire”.")
        b = 0
    else:
        # The b variable is to check if a strategy has been already chosen
        b = 1

# Checking if Strategy 3, aka Kill the King is suitable with the parameters inputted
if counter == 0:
    if time in no and number_soldiers >= 1 and poison in yes:
        print("The recommended strategy is C: “Kill the King”.")
        c = 0
    else:
        # The c variable is to check if a strategy has been already chosen
        c = 1

if a + b + c == 3:
    print("None of the three strategies is satisfied completely but I'll tell you what you satisfy for each of them "
          "right now so you can take a decision:")
    # Checking whether where time satisfies each attack condition
    if time in no:
        satisfyA = satisfyA + "Night"
        satisfyC = satisfyC + "Night"
        dn_satisfyB = dn_satisfyB + "Night"
    else:
        dn_satisfyA = dn_satisfyA + "Day"
        satisfyB = satisfyB + "Day"
        dn_satisfyC = dn_satisfyC + "Day"
    # Checking whether the number of soldiers satisfies each attack condition
    if number_soldiers >= 1:
        satisfyC = satisfyC + ", 1 soldier"
        if number_soldiers >= 500:
            satisfyA = satisfyA + ", more than 500 soldiers"
            if number_soldiers >= 10000:
                satisfyB = satisfyB + ", more than 10.000 soldiers"
            else:
                dn_satisfyB = dn_satisfyB + ", less than 10.000 soldiers"
        else:
            dn_satisfyA = dn_satisfyA + ", less than 500 soldiers"
    else:
        dn_satisfyC = dn_satisfyC + ", less than 1 soldier"
    # Checking whether the number of siege engines satisfies each attack condition
    if siege >= 50:
        satisfyA = satisfyA + ", at least 50 siege engines"
    else:
        dn_satisfyA = dn_satisfyA + ", less than 50 siege engines"
    # Checking if the use of poison satisfies each attack condition
    if poison in yes:
        satisfyC = satisfyC + ", poison"
    else:
        dn_satisfyC = dn_satisfyC + "Poison"

    print("Strategy A:\n" "\t\tSatisfy: " + satisfyA + "\n \t\tDoes not satisfy: " + dn_satisfyA, end=".\n")
    print("Strategy B:\n" "\t\tSatisfy: " + satisfyB + "\n \t\tDoes not satisfy: " + dn_satisfyB, end=".\n")
    print("Strategy C:\n" "\t\tSatisfy: " + satisfyC + "\n \t\tDoes not satisfy: " + dn_satisfyC, end=".")
