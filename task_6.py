"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа."""

import sys
import random
import collections

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100


def size_f(*args):
    sum_m = 0
    for k in args:
        sum_m += sys.getsizeof(k)
    return sum_m


# 1 - через массивы
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)
list_ch_1 = []
for i, item in enumerate(array_1):
    if item % 2 == 0:
        list_ch_1.append(i)
print(f'Индексы четных элементов: {list_ch_1}')
print(f'Необходимая память {size_f(array_1, list_ch_1)}')


# 2 - через очередь
dec = collections.deque(array_1)
print(dec)
dec_ch = collections.deque()
for i, item in enumerate(dec):
    if item % 2 == 0:
        dec_ch.append(i)
print(f'Индексы четных элементов: {dec_ch}')
print(f'Необходимая память {size_f(dec, dec_ch)}')


# 3 - через кортеж и список (не самы лучший вариант конечно)
tup = tuple(array_1)
print(tup)
list_ch_2 = []
for i, item in enumerate(tup):
    if item % 2 == 0:
        list_ch_2.append(i)
print(f'Индексы четных элементов: {list_ch_1}')
print(f'Необходимая память {size_f(tup, list_ch_2)}')

"""[86, 61, 95, 56, 15, 51, 37, 73, 37, 70]
Индексы четных элементов: [0, 3, 9]
Необходимая память 272
deque([21, 6, 79, 14, 92, 80, 82, 89, 25, 39])
Индексы четных элементов: deque([1, 3, 4, 5, 6])
Необходимая память 1248
(77, 83, 63, 80, 79, 42, 14, 20, 4, 36)
Индексы четных элементов: [0, 3, 9]
Необходимая память 240"""