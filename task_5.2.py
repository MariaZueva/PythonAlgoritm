"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция,
элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
from collections import deque

OSN = 16
dic_hex = {'0': 0, '1': 1, '2': 2,
           '3': 3, '4': 4, '5': 5,
           '6': 6, '7': 7, '8': 8,
           '9': 9, 'A': 10, 'B': 11,
           'C': 12, 'D': 13, 'E': 14, 'F': 15}
inv_dic_hex = {value: key for key, value in dic_hex.items()}


def sum_hex(a, b):
    na = deque()
    nb = deque()
    len_a = len(a)
    len_b = len(b)
    na.extend(a)
    nb.extend(b)
    if len_a > len_b:
        nb.extendleft('0' * (len_a - len_b))
    else:
        na.extendleft('0' * (len_b - len_a))
    # print(na)
    # print(nb)
    sum_el = deque()
    d = 0
    while len(na) > 0:
        tmp = dic_hex[na.pop()] + dic_hex[nb.pop()] + d
        if tmp >= OSN:
            d = 1
            tmp -= OSN
        else:
            d = 0
        sum_el.appendleft(inv_dic_hex[tmp])
    if d > 0:
        sum_el.appendleft(1)
    return sum_el


def mul_hex(a, b):
    na = deque(a)
    nb = deque(b)
    res_t = []
    ind = 0
    while len(nb) > 0:
        res_t.append(deque())
        curr_b = nb.pop()
        d = 0
        while len(na) > 0:
            tmp1 = dic_hex[na.pop()] * dic_hex[curr_b] + d
            d, m = divmod(tmp1, OSN)
            res_t[ind].appendleft(inv_dic_hex[m])
        if d > 0:
            res_t[ind].appendleft(inv_dic_hex[d])
        res_t[ind].extend('0' * ind)

        na.extend(a)
        ind += 1

    res = deque('0')
    for i in res_t:
        res = sum_hex(res, i)

    return res


def hex_deque(xt):
    hq = deque()
    for i in xt:
        if i in dic_hex:
            hq.append(i)
        else:
            return None
    return hq


x1 = hex_deque(str(input('Введите первое число = ')))
x2 = hex_deque(input('Введите второе число = '))

print(f'{list(x1)} + {list(x2)} = {list(sum_hex(x1, x2))}')
print(f'{list(x1)} * {list(x2)} = {list(mul_hex(x1, x2))}')

