"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""
import random


MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 10


def bubble_sort(array_sort):
    i = 0
    flag = True
    le = len(array_sort)
    while flag:
        flag = False
        for j in range(le - i - 1):
            if array_sort[j] < array_sort[j + 1]:
                array_sort[j], array_sort[j + 1] = array_sort[j + 1], array_sort[j]
                flag = True
        i += 1
    return array_sort


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
new_array = bubble_sort(array)
print(new_array)
