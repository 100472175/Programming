list1 = [1, 2, 3, 4, 5]
list1.append(7)
# list1 = [1,2,3,4,5,7]


list1.insert(2, 'hello')
# list1 = [1,2,'hello',3,4,5,7] Remember, python starts counting from 0
list1.insert(-2, 'bye')
# list1 = [1, 2, 'hello, 3, 4, 5, 'bye', 7]

list2 = ['a', 'b', 'c']
list1.extend(list2)
# list1 = [1, 2, 'hello, 3, 4, 5, 'bye', 7, 'a', 'b', 'c']

list1 = [1, 2, 3, 4, 1, 2]
list1.index(1)  # 0
list1.index(2)  # 1
list1.index(2, 2)  # 5
list1.index(2, list1.index(2)+1)


list1.count(2)  # 2

list1.remove(1)  # list1 = [2, 3, 4, 1, 2]

a = list1.pop(3)
print(a)

list1 = ['a', 'b', 'ab','azz', 'z', 'zz']  # alphabetical order: ['a', 'ab', 'azz', 'b', 'z', 'zz']
print(list1)
list1.sort()
print(list1)

list1 =[1, 5, 7, 23, 8, 9, 5, False]
list1.sort()  # [False, 1, 5, 5, 7, 8, 9, 23]
print(list1)


diccionario={asdf: qwert}
for a, b in diccionario.items():
