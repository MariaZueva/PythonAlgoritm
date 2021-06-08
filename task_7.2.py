"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""
import random


MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 10


def merge_s(arr, l, r):
    if l >= r:
        n_r = arr
        return n_r
    mid = (l + r - 1) // 2

    merge_s(arr, l, mid)
    merge_s(arr, mid + 1, r)
    s_mas = merge(arr, l, mid, r)
    return merge(arr, l, mid, r)


def merge(arr, s, m, e):
    l = s
    r = m + 1
    if arr[m] <= arr[r]:
        return arr
    while l <= m and r <= e:
        if arr[l] <= arr[r]:
            l += 1
        else:
            i = r
            tmp = arr[r]
            while i != l:
                arr[i] = arr[i - 1]
                i -= 1
            arr[l] = tmp
            l += 1
            r += 1
            m += 1


array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print(merge_s(array, 0, len(array) - 1))
