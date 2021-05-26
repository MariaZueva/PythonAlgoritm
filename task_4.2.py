import timeit


def my_simple(n):
    k = 1
    p_ch = 2
    while k < n:
        p_ch += 1
        for j in range(2, p_ch):
            if p_ch % j == 0:
                break
        else:
            k += 1
    return p_ch


def sive(n):
    size = n ** 2 + 3
    array = [i for i in range(size)]
    array[1] = 0
    for i in range(2, size):
        if array[i] != 0:
            j = i ** 2
            while j < size:
                array[j] = 0
                j += i
    result = []
    for i in array:
        if i != 0:
            result.append(i)
    return result[n - 1]


#  1  2  3  4  5   6   7   8   9
# [2, 3, 5, 7, 11, 13, 17, 19, 23]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


pr = int(input('Введите номер простого числа '))
print(my_simple(pr))
print(sive(pr))

print(f"Алгоритм {pr} - ое число без решета Эратосфена {timeit.timeit('my_simple(pr)', number=1000, globals=globals())}")
print(f"Алгоритм {pr} - ое число решето Эратосфена {timeit.timeit('sive(pr)', number=1000, globals=globals())}")

"""Алгоритм 100 - ое число без решета Эратосфена 1.5193060000000003
Алгоритм 100 - ое число решето Эратосфена 3.8139470000000006
Алгоритм 200 - ое число без решета Эратосфена 7.858929900000001
Алгоритм 200 - ое число решето Эратосфена 15.2871602
Алгоритм 300 - ое число без решета Эратосфена 20.167040200000002
Алгоритм 300 - ое число решето Эратосфена 37.7147065
"""