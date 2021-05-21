"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
import random

SIZE_M = 5
SIZE_N = 5
MIN_ITEM = 0
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
print(*matrix, sep='\n')

list_min_el = []
for i in range(SIZE_M):
    list_min_el.append(matrix[0][i])
    for j in range(1, SIZE_N):
        if list_min_el[i] > matrix[j][i]:
            list_min_el[i] = matrix[j][i]
max_el = list_min_el[0]
for i in list_min_el:
    if max_el < i:
        max_el = i
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_el}')

