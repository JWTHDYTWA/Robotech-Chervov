# Червов Андрей 001с1 — Робототехника. Списки и срезы.

L = int(input("Длина списка?\n"))
nums = [int(input("Элемент " + str(i) + ": ")) for i in range(L)]

# Если вместо range() будет сам nums, цикл выведет только
# половину элементов, т.к. счетчик [i] будет идти с левого края,
# а удаление элементов методом list.pop будет двигать правую
# границу списка

for i in range(len(nums)):
    print(nums.pop(nums.index(max(nums))))

# Запрета на очистку списка в задании не было
