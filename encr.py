keys = {'1': '7', '2': '3', '3': '2', '4': '6', '5': '9', '6': '0', '7': '1', '8': '5', '9': '4', '0': '8'}

# Экспорт словаря в файл
def expd(keys):
    d = open('dict.txt', 'wt')
    d.write(str(keys))
    d.close()

# Импорт словаря из файла (не обязательно,
# по умолчанию используется словарь из первой строки)
def impd(keys):
    d = open('dict.txt', 'rt')
    nkeys = eval(d.read())
    keys.update(nkeys)
    d.close()

# Функция шифровки
def enc():
    msgi = input('Сообщение: ')
    msgo = ''
    for i in range(len(msgi)):
        if keys.get(msgi[i]) == None:
            continue
        msgo = msgo + str(keys.get(msgi[i]))
    print('Шифр: ' + msgo)

# Функция расшифровки
def dec():
    ikeys = {o:i for i, o in keys.items()}
    enci = input('Шифр: ')
    deco = ''
    for i in range(len(enci)):
        deco = deco + ikeys.get(enci[i])
    print('Сообщение: ' + deco)

while 1:
    tmp = input('\n"enc" = зашифровать\n"dec" = расшифровать\n"export" = экспорт словаря в файл\n"import" = импортировать словарь из файла\n\nДействие: ')
    if tmp == 'enc':
        enc()
    elif tmp == 'dec':
        dec()
    elif tmp == 'export':
        expd(keys)
        print('Словарь сохранён в dict.txt')
    elif tmp == 'import':
        impd(keys)
        print('Словарь считан из dict.txt')
    elif tmp == 'debug':
        print(str(keys))
