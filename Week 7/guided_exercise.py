import random
number_soldiers = 10_000
# lanniester = attackers = triagnle

min_power = 10
max_power = 99

counter = 0

attackers = []
defenders = []
lannister_formation = []
triangle_formation = [1_000, 2_000, 3_000, 4_000]

"""for i in range(number_soldiers):
    attackers.append(random.randint(min_power, max_power))
    defenders.append(random.randint(min_power, max_power))
for _ in range(4):
    lannister_formation.append([])"""

for soldiers in range(number_soldiers):
    if soldiers == 0 or soldiers == 1000 or soldiers == 3000 or soldiers == 6000:
        lannister_formation.append([])
    lannister_formation[-1].append(random.randint(10, 99))



"""

# lannister_formation.append([])
for n in range(1_000):
    lannister_formation[0].append(attackers[n])

# lannister_formation.append([])
for n in range(1_000, 3_000):
    lannister_formation[1].append(attackers[n])

# lannister_formation.append([])
for n in range(3_000, 6_000):
    lannister_formation[2].append(attackers[n])

# lannister_formation.append([])
for n in range(6_000, 10_000):
    lannister_formation[3].append(attackers[n])
"""

# Baratheon = defenders
number_soldiers = 10_000
rows_bara = 8
baratheon_formation = [[]]
soldier_per_row = number_soldiers // rows_bara

# for i in range(rows_bara):
    # baratheon_formation.append([])

for i in range(soldier_per_row):
    if i == soldier_per_row:
        baratheon_formation.append([])
    baratheon_formation[-1].append(random.randint(10, 99))

print(soldier_per_row)



