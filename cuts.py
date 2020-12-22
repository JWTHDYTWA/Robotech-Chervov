# Червов Андрей 001с1 — Задание 3: Срезы
import random
list1 = [ random.randint(0, 9) for i in range(9) ]

# Среднее значение
avg = 0
for i in range(len(list1)):
    avg = avg + list1[i]
avg = int(avg / len(list1))

# Поиск ближайшего значения в списке
# Если элемента со средним значением нет в списке,
# проверяются avg-1, avg+1, avg-2, avg+2, avg-3 ..
cnt = -1
favg = avg
while favg not in list1:
    favg += cnt
    if cnt % 2 == 0:
        cnt = -cnt - 1
    else:
        cnt = -cnt + 1

print('Изначальный список: ' + str(list1))
print('Среднее арифметическое: ' + str(avg))
print('Ближайшее найденное значение: ' + str(favg))

# Формирование среза
cut1 = []
if list1.index(favg) != 0:
    cut1 = list1[:list1.index(favg)]
list1.clear()
for i in range(len(cut1)):
    list1.append(cut1[i])
list1.append(avg)
for i in range(len(cut1)):
    list1.append(cut1[i])
print('Обработанный массив: ' + str(list1))
