"""В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = 0
ind_max_negative = None
fl = False
for i, elem in enumerate(array):
    if elem < 0:
        if elem > max_negative and fl or not fl:
            max_negative = elem
            ind_max_negative = i
            fl = True

if max_negative != 0:
    print(f'Максимальный отрицательный элемент в массиве = {max_negative}, его индекс {ind_max_negative}')
else:
    print('В массиве отсутствуют отрицательные элементы')
