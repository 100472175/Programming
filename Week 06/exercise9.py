"""
Exercise 9
@Author : Eduardo Alarcón
@version: 1.0
@Date : 14-10-21
Instructions: Gymnast scores
"""
import random

scores_list = []
for i in range(5):
    scores_list.append(random.randint(1, 10))
    print('Judge %i gave the gymnast a score of %i points' % (i+1, scores_list[i]))
scores_list.sort()
scores_list.reverse()
print('The maximum score the gymnast has obtained is %i and the lowest one is %i' % (scores_list[0], scores_list[-1]))
