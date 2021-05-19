"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""
# https://drive.google.com/file/d/10acIHZb8Q8ltP5RHP40PW7k4c1_66o_H/view?usp=sharing


def sum_pos(n):
    if n == 1:
        return 1
    else:
        return 1 - sum_pos(n - 1) * 0.5


num = int(input('Введите количество членов ряда n = '))
print(f'1 + (-0.5) + 0.25 + ... + (n-1) * (-0.5) = {sum_pos(num)}')

