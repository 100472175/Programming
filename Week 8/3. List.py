import random
elements, list1 = random.randrange(10, 15), []
while len(list1) < elements:
    new = random.randrange(elements * 2)
    if new not in list1:
        list1.append(new)

print("The list is", list1)
for i in range(len(list1)):
    if i % 2 == 0 and list1[i] % 2 != 0:
        list1[i] += 1
    list1[i] += 1
print("The new list is", list1)

# Final answer :
'''
10
2
17
    14
    9
        11
15        
6
7
12
3
13
16
'''