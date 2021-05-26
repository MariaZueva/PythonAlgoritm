"""Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Задача:
    Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

import random
import timeit
import cProfile


def decision_one(matrix):
    list_min_el = []
    m = len(matrix[0])
    n = len(matrix)
    for i in range(m):
        list_min_el.append(matrix[0][i])
        for j in range(1, n):
            if list_min_el[i] > matrix[j][i]:
                list_min_el[i] = matrix[j][i]
    max_el = list_min_el[0]
    for i in list_min_el:
        if max_el < i:
            max_el = i
    return max_el


def decision_two(matrix):
    max_ = None
    for j in range(len(matrix[0])):
        min_ = matrix[0][j]
        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
        if max_ is None or max_ < min_:
            max_ = min_
    return max_


def decision_three(matrix):
    new_m = len(matrix)
    new_n = len(matrix[0])
    new_matrix = []
    for i in range(new_n):
        new_matrix.append([])
        for j in range(new_m):
            new_matrix[i].append(matrix[j][i])
    max_min = None
    for i in new_matrix:
        min_ = min(i)
        if max_min is None or max_min < min_:
            max_min = min_
    return max_min


for k in (5, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240):
    SIZE_M = k
    SIZE_N = k
    MIN_ITEM = -100
    MAX_ITEM = 100
    mx = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
    # print(*mx, sep='\n')
    print(f"первый алгоритм с {k}*{k} элементами {timeit.timeit('decision_one(mx)', number=1000, globals=globals())}")
    print(f"второй алгоритм с {k}*{k} элементами {timeit.timeit('decision_two(mx)', number=1000, globals=globals())}")
    print(f"третий алгоритм с {k}*{k} элементами {timeit.timeit('decision_three(mx)', number=1000, globals=globals())}")

"""первый алгоритм с 5*5 элементами 0.0037938
второй алгоритм с 5*5 элементами 0.003550500000000005
третий алгоритм с 5*5 элементами 0.007733900000000002
первый алгоритм с 20*20 элементами 0.037979399999999996
второй алгоритм с 20*20 элементами 0.0318006
третий алгоритм с 20*20 элементами 0.04847180000000001
первый алгоритм с 40*40 элементами 0.1479263
второй алгоритм с 40*40 элементами 0.12144949999999999
третий алгоритм с 40*40 элементами 0.17949550000000003
первый алгоритм с 60*60 элементами 0.3058712
второй алгоритм с 60*60 элементами 0.2608615000000001
третий алгоритм с 60*60 элементами 0.3946984
первый алгоритм с 80*80 элементами 0.5238896
второй алгоритм с 80*80 элементами 0.4454393999999997
третий алгоритм с 80*80 элементами 0.7187090999999999
первый алгоритм с 100*100 элементами 0.8246014000000002
второй алгоритм с 100*100 элементами 0.7002896999999999
третий алгоритм с 100*100 элементами 1.0906311999999998
первый алгоритм с 120*120 элементами 1.1737111999999996
второй алгоритм с 120*120 элементами 0.9903389000000002
третий алгоритм с 120*120 элементами 1.6107389999999988
первый алгоритм с 140*140 элементами 1.5598082999999985
второй алгоритм с 140*140 элементами 1.3289473000000012
третий алгоритм с 140*140 элементами 2.200694799999999
первый алгоритм с 160*160 элементами 1.9700693000000005
второй алгоритм с 160*160 элементами 1.6959238000000028
третий алгоритм с 160*160 элементами 2.8658503999999994
первый алгоритм с 180*180 элементами 2.558768099999998
второй алгоритм с 180*180 элементами 2.1436515999999983
третий алгоритм с 180*180 элементами 3.5655371000000002
первый алгоритм с 200*200 элементами 3.2218772000000016
второй алгоритм с 200*200 элементами 2.6367626999999985
третий алгоритм с 200*200 элементами 4.426929300000005
первый алгоритм с 220*220 элементами 3.863643400000001
второй алгоритм с 220*220 элементами 3.2250345000000067
третий алгоритм с 220*220 элементами 5.341991700000001
первый алгоритм с 240*240 элементами 4.476642499999997
второй алгоритм с 240*240 элементами 3.794116899999999
третий алгоритм с 240*240 элементами 6.425892500000003

Из полученных результатов и самих алгоритмов видим, чтовсе алгоритмы имеют сложность О(n^2).
Самый оптимальный второй, т.к. там происходит всего один проход циклов (внешний внетренний) (в первом
алгоритме осуществляется дополгительный проход для поиска максимального эл-та, и 
не происходит выделения достаточно большого объема 
дополнительной памяти как в третьем (транспонирование матрицы)
"""

print()

SIZE_M = 1000
SIZE_N = 1000
MIN_ITEM = -100
MAX_ITEM = 100
mx_ = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
cProfile.run('decision_one(mx_)')

"""1006 function calls in 0.141 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.141    0.141 <string>:1(<module>)
        1    0.141    0.141    0.141    0.141 task_4.1.py:17(decision_one)
        1    0.000    0.000    0.141    0.141 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

print()
cProfile.run('decision_two(mx_)')
"""1005 function calls in 0.128 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.128    0.128 <string>:1(<module>)
        1    0.127    0.127    0.128    0.128 task_4.1.py:33(decision_two)
        1    0.000    0.000    0.128    0.128 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""

print()
cProfile.run('decision_three(mx_)')

"""1002006 function calls in 0.487 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.007    0.007    0.487    0.487 <string>:1(<module>)
        1    0.336    0.336    0.480    0.480 task_4.1.py:45(decision_three)
        1    0.000    0.000    0.487    0.487 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.027    0.000    0.027    0.000 {built-in method builtins.min}
  1001000    0.118    0.000    0.118    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""