# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:33:33 2019

@author: Programming Professors. UC3M.
@version: 1.0
"""
# We start by asking the user about the data
# With lower we convert the input str to lower case
# That way we don't mind if "day" "DAY" "Day" etc is entered
day = input("Is day or night? ").lower()
# For soldiers and engines we need to cast to int
soldiers = int(input("Number of soldiers? "))
engine = int(input("Engines? "))
# Casting to boolean does not work as expected (any non-empty str is True),
# so we will do the casting manually
poison = input("Do you have poison? (True/False) ")
rain = input("It is raining (True/False) ").lower()

# It is better to lower the input, but we can also do it here.
# Notice that poison is only lowered for the comparison, the str
# it stores does not vary
if poison.lower() == "true":
    # Notice we are changing the type of poison here, usually changing the type
    # of a variable is not a good idea as resulting code is confusing, but here
    # we wanted poison to be boolean and it was str only because of the input
    poison = True
else:
    poison = False

# To commpare strings is usually better to use "in", that way we cover cases
# like "true " " true " " true" "yes it is true", etc.
if "true" in rain:
    rain = True
else:
    rain = False

# Now we check the conditions for strategyA, instead of rain == false we use
# not rain. Notice the () are optional, but compulsory if we split the if in
# more than one line
if (day == "night" and not rain
        and soldiers >= 500 and engine >= 50):
    print('The recommended strategy is A:"Silent attack"')
# If A is not valid, we check B. Notice that using elif only one will be valid:
# if A and B are valid, we will print just A. The problem says nothing, so we
# can choose the behavior
elif day == "day" and soldiers > 10_000:
    print('The recommended strategy is B:"Crossfire"')
# Now checking C
elif day == "night" and soldiers >= 1 and poison:
    print('The recommended strategy is C:"Kill the King"')
else:
    # As none is satisfied we need to say what is missing
    # String variables to store what we have and what is missing
    satA = satB = satC = " "
    unSatA = unSatB = unSatC = " "
    # Checking if it is day
    if day == "day":
        unSatA += "night, "
        satB += "day, "
        unSatC += "night, "
    else:
        satA += "night, "
        unSatB += "day, "
        satC += "night, "
    # Checking the rain, it only affects A
    if not rain:
        satA += "no rain, "
    else:
        unSatA += "no rain, "
    # Soldiers affect A, B and C, but with different conditions
    if soldiers >= 500:
        satA += "at least 500 soldiers, "
    else:
        unSatA += "at least 500 soldiers, "

    if soldiers > 10_000:
        satB += "more than 10,000 soldiers, "
    else:
        unSatB += "more than 10,000 soldiers, "

    if soldiers >= 1:
        satC += "one soldier, "
    else:
        unSatC += "one soldier, "

    # Engines is only for A
    if engine >= 50:
        satA += "at least 50 siege engines, "
    else:
        unSatA += "at least 50 siege engines, "

    # Poison only for C
    if poison:
        satC += "poison, "
    else:
        unSatC += "poison, "

    # Now we erase the last  " ," and add a .
    satA = satA+"\b\b."
    unSatA = unSatA+"\b\b."
    satB = satB+"\b\b."
    unSatB = unSatB+"\b\b."
    satC = satC+"\b\b."
    unSatC = unSatC+"\b\b."

    print("None of the three strategies is satisfied completely but I'll"
          + " tell you what you satisfy for each one of them right now so you"
          + " can take a decision:\n")
    print("Strategy A:\n\tSatisfy: %s" % satA)
    print("\tDo not satisfy: %s" % unSatA)
    print("Strategy B:\n\tSatisfy: %s" % satB)
    print("\tDo not satisfy: %s" % unSatB)
    print("Strategy C:\n\tSatisfy: %s" % satC)
    print("\tDo not satisfy: %s" % unSatC)

    # This is the point where the exercise 3 code begins

    # We declare some constants to make the code more readable. Also if the
    # values need to be changed we will only change them here, not everywhere
    # they are used
    SOLDIER_COINS = 10
    MACHINE_WOOD = 200
    MACHINE_IRON = 50
    POISON_WOOD = 100
    POISON_HERBS = 50
    POISON_COINS = 100
    MINIMUM_WOOD = 20
    WOOD_COINS = 10
    MINIMUM_HERBS = 10
    HERBS_COINS = 10
    MINIMUM_IRON = 5
    IRON_COINS = 10
    GIFT = 10
    SOLDIERS_GIFT = 5
    # We create also a variable for the money, we don't declare it as a
    # constant as we will decrement it while buying things
    money = 10_000
    # Generating a random strategy
    # It is better if we import random at the beginning of our program
    import random
    # We will use an integer variable to code strategies: 0 = A, 1 = B, 2 = C
    # We create constants to denote which is each strategy
    STRATEGY_A = 0
    STRATEGY_B = 1
    STRATEGY_C = 2
    strategy = random.randrange(0, 3)
    # Creating variables for the needs
    soldiersMissing = machinesMissing = 0
    woodNeeded = ironNeeded = 0
    # The materials I have
    wood = iron = herbs = 0
    # For A we need 500 soldiers and 50 machines
    if strategy == STRATEGY_A:
        soldiersMissing = 500 - soldiers
        machinesMissing = 50 - engine
        # to avoid printing negative numbers
        if (soldiersMissing < 0):
            soldiersMissing = 0
        if (machinesMissing < 0):
            machinesMissing = 0
        print("\nWe will follow strategy A. I will buy things for you.")
        print("You need to buy %i soldiers and %i siege machines"
              % (soldiersMissing, machinesMissing))
    # For B more than 10_000 soldiers
    elif strategy == STRATEGY_B:
        soldiersMissing = 10_001 - soldiers
        print("We will follow strategy B. I will buy soldiers for you.")
        print("You need to buy %i soldiers" % soldiersMissing)
    # For C 1 soldier and poison
    else:
        soldiersMissing = 1 - soldiers
        # to avoid printing negative numbers
        if (soldiersMissing < 0):
            soldiersMissing = 0
        print("We will follow strategy C. I will buy things for you.")
        print("You need to buy %i soldiers and poison" % soldiersMissing)

    # We start by buying soldiers, we keep buying while we still need soldiers
    # and we have money enough. We count the soldiers bought so we know how
    # many wood we will receive as a gift. Notice that if soldiersMissing is
    # <= 0 the loop will be skipped
    soldiersBought = 0
    while soldiersMissing > 0 and money >= SOLDIER_COINS:
        soldiersMissing -= 1
        money -= SOLDIER_COINS
        soldiersBought += 1
        print("1 soldier was bought. %i golden coins were used."
              % SOLDIER_COINS)
        # We calculate the wood received as gift
        if soldiersBought % SOLDIERS_GIFT == 0:
            wood += GIFT

    # Now we do the same for machines, if no machines needed this will be
    # skipped
    if machinesMissing > 0:
        # Calculating wood and iron needed
        woodNeeded = machinesMissing * MACHINE_WOOD - wood
        ironNeeded = machinesMissing * MACHINE_IRON

        # Buying wood
        while woodNeeded > 0 and money >= WOOD_COINS:
            wood += MINIMUM_WOOD
            woodNeeded -= MINIMUM_WOOD
            money -= WOOD_COINS
            print("%i wood bought. %i golden coins were used" % (MINIMUM_WOOD,
                                                                 WOOD_COINS))

        # Buying iron
        while ironNeeded > 0 and money >= IRON_COINS:
            iron += MINIMUM_IRON
            ironNeeded -= MINIMUM_IRON
            money -= IRON_COINS
            print("%i iron bought. %i golden coins were used" % (MINIMUM_IRON,
                                                                 IRON_COINS))
        # Now we buy the machines
        while (machinesMissing > 0 and wood >= MACHINE_WOOD
               and iron >= MACHINE_IRON):
            machinesMissing -= 1
            engine += 1
            wood -= MACHINE_WOOD
            iron -= MACHINE_IRON
            print("1 siege machine bought. %i wood and %i iron were used"
                  % (MACHINE_WOOD, MACHINE_IRON))

    # Finally buying the poison, we also check if we have money and the soldier
    if (strategy == STRATEGY_C and not poison and money >= POISON_COINS
            and soldiers >= 1):
        money -= POISON_COINS
        # If we needed a soldier it has already been bought, or we had no money
        # we need to buy wood and herbs
        while wood < POISON_WOOD and money >= WOOD_COINS:
            wood += MINIMUM_WOOD
            money -= WOOD_COINS
            print("%i wood bought. %i golden coins were used" % (MINIMUM_WOOD,
                                                                 WOOD_COINS))
        while herbs < POISON_HERBS and money >= HERBS_COINS:
            herbs += MINIMUM_HERBS
            money -= HERBS_COINS
            print("%i herbs bought. %i golden coins were used"
                  % (MINIMUM_HERBS, HERBS_COINS))

        # buying the poison
        if herbs >= POISON_HERBS and wood >= POISON_WOOD:
            poison = True

    # Now we check if we could do it or not
    if strategy == STRATEGY_A:
        if soldiersMissing == 0 and machinesMissing == 0:
            print("I bought, everything you needed for A. Let's do it")
            print("You still have %i gold coins" % money)
        else:
            print("Sorry, you got out of money for A")
            print("You still need %i soldiers and %i siege machines"
                  % (soldiersMissing, machinesMissing))
    elif strategy == STRATEGY_B:
        if soldiersMissing == 0:
            print("I bought, everything you needed for B. Let's do it")
            print("You still have %i gold coins" % money)
        else:
            print("Sorry, you got out of money for B")
            print("You still need %i soldiers" % soldiersMissing)
    else:
        if poison:
            print("I bought, everything you needed for C. Let's do it")
            print("You still have %i gold coins" % money)
        else:
            print("Sorry, you got out of money")
            print("I cannot buy the ingredients for the poison")