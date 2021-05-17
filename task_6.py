"""Пользователь вводит номер буквы в алфавите. Определить, какая это буква"""
# https://drive.google.com/file/d/1Niz_pp9UiCiOnihNseReXbUnyvjV05Je/view?usp=sharing


a = int(input('Введите номер буквы в алфавите = '))
cod = a + 96
if 96 < cod < 123:
    ch = chr(cod)
    print(f'Номер {a} имеет буква {ch}')
else:
    print('Введенное число не является номером буквы в алфавите a-z')


