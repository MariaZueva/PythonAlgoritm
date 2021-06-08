"""Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше ее."""
import random


def median(mass):
    for i in range(len(mass)):
        s = 0
        e = 0
        b = 0
        for j in range(len(mass)):
            if mass[i] < mass[j]:
                s += 1
            elif mass[i] > mass[j]:
                b += 1
            else:
                e += 1
        e -= 1

        if s == b or s == e + b or b == e + s or (e > 1 and abs(b - s) < e):
            return mass[i]


SIZE = 10
MAX = 10
arr = [random.randrange(0, MAX) for _ in range(2 * SIZE + 1)]


print(arr)
print(f'Медиана = {median(arr)}')

