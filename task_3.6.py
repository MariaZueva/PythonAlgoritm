"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
 элементами. Сами минимальный и максимальный элементы в сумму не включать."""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

ind_min_elem = 0
min_el = array[ind_min_elem]
ind_max_elem = 0
max_el = array[ind_max_elem]
for i, elem in enumerate(array):
    if min_el > elem:
        min_el = elem
        ind_min_elem = i
    elif max_el < elem:
        max_el = elem
        ind_max_elem = i

print(f'Минимальный элемент = {min_el} на позиции {ind_min_elem}')
print(f'Максимальный элемент = {max_el} на позиции {ind_max_elem}')

k = 1 if ind_max_elem > ind_min_elem else -1

s = 0
if min_el == max_el:
    print('Минимальный и максимальный элементы совпадают')
else:
    for i in range(ind_min_elem + k, ind_max_elem, k):
        s += array[i]
    print(f'Сумма между элементами {s}')
