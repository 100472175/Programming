"""
Exercise 5
@Author : Eduardo Alarcón
@version: 1.0
@Date : 21-10-21
Instructions: Create three dictionaries: maria, peter, and mike. Give each dictionary the keys ’name’, ’weeklyExercises’
 and ’weeklyTests. Have the ’name’ key be the name of the student (that is, maria’s name should be ’Maria’ and so on).
 The other keys should be an empty list. Print the dictionaries on the screen. Next populate each list with 10 random
 numbers in the range 0 to 10. For each of the dictionaries create a new key named exam and fill it with a random value
  in the range 0 to 10.
"""
import random
def printing():
    print(maria)
    print(peter)
    print(mike)


maria = {'name': 'Maria', 'weeklyExercise': [], 'weeklyTests': []}
peter = {'name': 'Peter', 'weeklyExercise': [], 'weeklyTests': []}
mike = {'name': 'Mike', 'weeklyExercise': [], 'weeklyTests': []}
people = (maria, peter, mike)

printing()

for e in people:
    for _ in range(10):
        e['weeklyExercise'].append(random.randint(0, 10))
        e['weeklyTests'].append(random.randint(0, 10))
for e in people:
    e['exam'] = random.randint(0, 10)

printing()
