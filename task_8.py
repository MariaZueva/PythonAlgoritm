"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""

import hashlib


def search_n_str(oll_str):
    set_s = set()
    for i in range(0, len(oll_str)):
        for j in range(i, len(oll_str) + 1):
            set_s.add(hashlib.sha1(oll_str[i:j].encode('utf-8')).hexdigest())
    # print(set_s)
    return len(set_s) - 2


my_s = input('Введите строку: ')
print(search_n_str(my_s))
