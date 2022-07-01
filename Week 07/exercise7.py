"""
Exercise 7
@Author : Eduardo Alarcón
@version: 1.0
@Date : 21-10-21
Instructions:

"""
import random

maria = {'name': 'Maria', 'weeklyExercise': [], 'weeklyTests': []}
peter = {'name': 'Peter', 'weeklyExercise': [], 'weeklyTests': []}
mike = {'name': 'Mike', 'weeklyExercise': [], 'weeklyTests': []}
people = (maria, peter, mike)

for e in people:
    for _ in range(10):
        e['weeklyExercise'].append(random.randint(0, 10))
        e['weeklyTests'].append(random.randint(0, 10))
for e in people:
    e['exam'] = random.randint(0, 10)
# Getting the average

for i in range(len(people)):
    people[i]['weeklyExercise'].append(sum(people[i]['weeklyExercise']) / len(people[i]['weeklyExercise']))
    people[i]['weeklyExercise'].append(max(people[i]['weeklyExercise']))
    people[i]['weeklyExercise'].append(min(people[i]['weeklyExercise']))

for i in range(len(people)):
    people[i]['weeklyTests'].append(sum(people[i]['weeklyTests']) / len(people[i]['weeklyTests']))
    people[i]['weeklyTests'].append(max(people[i]['weeklyTests']))
    people[i]['weeklyTests'].append(min(people[i]['weeklyTests']))

    # people[i]['mark'] = [people[i]['weeklyExercise'][-3]*0.1 + people[i]['weeklyTests'][-3]*0.3 + people[i]['exam']*0.6]
for i in people:
    i['mark'] = i['weeklyExercise'][-3] * 0.1 + i['weeklyTests'][-3] * 0.3 + i['exam'] * 0.6

"""maria['mark'] = maria['weeklyExercise'][-3]*0.1 + maria['weeklyTests'][-3]*0.3 + maria['exam']*0.6
peter['mark'] = peter['weeklyExercise'][-3]*0.1 + peter['weeklyTests'][-3]*0.3 + peter['exam']*0.6
mike['mark'] = peter['weeklyExercise'][-3]*0.1 + peter['weeklyTests'][-3]*0.3 + peter['exam']*0.6
"""
assign = ''
for i in people:
    if i['mark'] >= 9:
        assign = 'A'
    elif i['mark'] >= 8:
        assign = 'B'
    elif i['mark'] >= 7:
        assign = 'C'
    elif i['mark'] >= 6:
        assign = 'D'
    elif i['mark'] >= 5:
        assign = 'E'
    else:
        assign = 'F'
    i['letterGrade'] = assign

keys = list(maria.keys())
print(keys)
keys = keys[10:-2]

print(
    " \nName:" + maria['name'] +
    " \nweeklyExercise: " + str(list(maria['weeklyExercise'])) +
    " \nweeklyTests: " + str(list(maria['weeklyTests'])) +
    " \nexam: " + str(maria['exam']) +
    " \nmark: " + str(maria['mark']) +
    " \nletterGrade: " + maria['letterGrade']
)
print(
    " \nName:" + peter['name'] +
    " \nweeklyExercise: " + str(list(peter['weeklyExercise'])) +
    " \nweeklyTests: " + str(list(peter['weeklyTests'])) +
    " \nexam: " + str(peter['exam']) +
    " \nmark: " + str(peter['mark']) +
    " \nletterGrade: " + peter['letterGrade']
)
print(
    " \nName:" + mike['name'] +
    " \nweeklyExercise: " + str(list(mike['weeklyExercise'])) +
    " \nweeklyTests: " + str(list(mike['weeklyTests'])) +
    " \nexam: " + str(mike['exam']) +
    " \nmark: " + str(mike['mark']) +
    " \nletterGrade: " + mike['letterGrade']
)
class_average = (maria['mark'] + peter['mark'] + mike['mark']) / len(people)
print("\n\nThe average of the class is: %.2f" % class_average)
