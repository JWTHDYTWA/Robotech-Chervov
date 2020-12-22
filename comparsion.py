import random

# Генерация списков
list_1 = [ random.randint(-20,20) for i in range(15) ]
list_2 = [ random.randint(-20,20) for i in range(15) ]
while 1:
    c = 0
    for i in range(len(list_2)):
        if list_1.count(list_2[i]):
            c += 1
    if c > 3:
        break
    list_2.insert(random.randint(0,14), random.randint(-20,20))

# Создание побочных списков
sublist_1 = []
sublist_2 = []
for i in range(len(list_1)):
    if list_2.count(list_1[i]) > 0:
        sublist_1.append(list_1[i])
for i in range(len(list_1)):
    if list_2.count(list_1[i]) == 0:
        sublist_2.append(list_1[i])

# Вывод
print('1st list: ', list_1, '\n2nd list:', list_2, '\nShared elements: ', sublist_1, '\nUnique for 1nd list: ', sublist_2)
