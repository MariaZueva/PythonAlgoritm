# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1Niz_pp9UiCiOnihNseReXbUnyvjV05Je/view?usp=sharing

a = int(input('Введите трехзначное число: '))

b = a % 10
a -= b
a = a // 10

c = a % 10
a -= c
a = a // 10

d = a % 10
a -= d
a = a // 10

s = b + c + d
m = b * c * d

print(f'Сумма цифр числа: {d} + {c} + {b} = {s}')
print(f'Произведенеи цифр числа: {d} * {c} * {b} = {m}')



