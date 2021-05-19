"""Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""
# https://drive.google.com/file/d/10acIHZb8Q8ltP5RHP40PW7k4c1_66o_H/view?usp=sharing

start = 32
stop = 127
pr = 10
for i in range(start, stop + 1):
    print(f'{i:3}:{chr(i):3}', end=' ', )
    if (i - start + 1) % pr == 0:
        print()

