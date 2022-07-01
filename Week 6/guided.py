"""
Guided Exercise
@Author : Eduardo Alarcón
@version: 1.0
"""
import random

attack_soldiers = 10_000
defend_soldiers = 3_201
list_defend = []
list_attack = []

for _ in range(1, defend_soldiers):
    list_defend.append((random.randint(10, 50) + 25))
for _ in range(1, attack_soldiers):
    list_attack.append(random.randint(10, 50))

defender = 0
attacker = 0
while attacker < len(list_attack) and defender < len(list_defend):
    defender = attacker % len(list_defend)
    if list_attack[attacker] > list_defend[defender]:
        list_attack[attacker] -= list_defend[defender] // 3
        del(list_defend[defender])
        attacker += 1
    else:
        list_defend[defender] -= list_attack[attacker] // 3
        del(list_attack[attacker])
        defender += 1
    if defender == len(list_defend):
        defender = 0
print('End of first wave'
    'Stannis: %i alive soldiers'
    'Lannister: %i alive soldiers')
