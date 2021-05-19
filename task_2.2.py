""" Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""
# https://drive.google.com/file/d/10acIHZb8Q8ltP5RHP40PW7k4c1_66o_H/view?usp=sharing

OSN = 10
num = int(input('Введите натуральное число '))
odd = 0
even = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // OSN
print(f'Четных чисел: {even}, нечетных чисел: {odd}')

