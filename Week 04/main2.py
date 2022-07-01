"""
Guided Exercise 2 : Battle strategies
@Author: Eduardo Alarcón
@version : 2.0
"""

# Recommendation: adding .lower to the end of an input, we avoid having to add it to every comparison
day: str = input("Are you attacking by day or night? ").lower()
soldiers: int = int(input("What are the number of soldiers on our side? "))
engines: int = int(input("What is the number of siege engines? "))
# Warning: any non-empty string will be True, even the str 'False'
poison: bool = bool(input("Are we going to use poison? (Press enter for No) "))
rain: str = input("Is it raining? ")
# print(day, soldiers, engines, poison, rain) # To check is the variables are correct
# If we want a boolean to be false, entered like an input, we need to leave it empty, press enter

satisfied = False
if (day.lower() == 'night'
        and soldiers >= 500
        and engines >= 50
        and rain.lower() == 'no'):
    print('The best strategy is A: "Silent attack".')
    satisfied = True
if (day.lower() == 'day'
        and soldiers > 10_000):
    print('The best strategy is B: "Crossfire".')
    satisfied = True
if (day.lower() == 'night'
        and soldiers >= 1
        and poison):
    print('The best strategy is C: "Kill the king".')
    satisfied = True

if not satisfied:
    satA = satB = satC = ''
    unSatA = unSatB = unSatC = ''
    print("None of the three strategies is satisfied completely but I'll tell you what you satisfy"
          "for each of them right now so you can take a decision:")

    # Checking whether where time satisfies each attack condition
    if day.lower() == 'night':
        satA = satA + 'Night time, '
        unSatB = unSatB + 'Night time, '
        satC = satC + 'Night time, '
    else:
        unSatA = unSatA + 'Day time, '
        satB = satB + 'Day time, '
        unSatC = unSatC + 'Day time, '

    # Checking whether the number of soldiers satisfies each attack condition
    if soldiers >= 1:
        satC = satC + '1 soldier, '
    else:
        unSatC = unSatC + 'less than 1 soldier, '
    if soldiers >= 500:
        satA = satA + 'more than 500 soldiers, '
    else:
        unSatA = unSatA + 'less than 500 soldiers, '
    if soldiers >= 10000:
        satB = satB + 'more than 10.000 soldiers '
    else:
        unSatB = unSatB + 'less than 10.000 soldiers '

    # Checking whether the number of siege engines satisfies each attack condition
    if engines >= 50:
        satA = satA + 'at least 50 siege engines, '
    else:
        unSatA = unSatA + 'less than 50 siege engines, '

    # Checking if the use of poison satisfies each attack condition
    if poison:
        satC = satC + "poison, "
    else:
        unSatC = unSatC + "poison, "

    print("Strategy A:\n" "\t\tSatisfy: " + satA[:-2] + "\n \t\tDoes not satisfy: " + unSatA[:-2], end='.\n')
    print("Strategy B:\n" "\t\tSatisfy: " + satB[:-2] + "\n \t\tDoes not satisfy: " + unSatB[:-2], end='.\n')
    print("Strategy C:\n" "\t\tSatisfy: " + satC[:-2] + "\n \t\tDoes not satisfy: " + unSatC[:-2], end='.')
