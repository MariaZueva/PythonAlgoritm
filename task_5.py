"""Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв"""
# https://drive.google.com/file/d/1Niz_pp9UiCiOnihNseReXbUnyvjV05Je/view?usp=sharing


a = input('Введите первую букву = ')
b = input('Введите вторую букву = ')
a_num = ord(a) - 96
b_num = ord(b) - 96

if a == b:
    print(f'Введенные буквы совпадают и находятся на месте {a_num}. Их расположение совпадает')
else:
    if a_num > b_num:
        gap = a_num - b_num - 1
    else:
        gap = b_num - a_num - 1
    print(f'Буква {a} находится на месте {a_num}')
    print(f'Буква {b} находится на месте {b_num}')
    print(f'Между ними {gap} букв')

