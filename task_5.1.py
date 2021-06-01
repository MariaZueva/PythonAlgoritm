"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего."""
from collections import namedtuple

Q = 4

Comp = namedtuple('Comp', ['name', 'profit_q', 'profit_oll'])
companies = []
profit_oll_comp_av = 0

n = int(input('Введите количество предприятий = '))
for i in range(n):
    c_name = input(f'Введите наименование {i + 1} - го предприятия: ')
    c_dic = dict()
    c_oll_p = 0
    for j in range(Q):
        p = float(input(f'Введите прибыль за {j + 1} квартал: '))
        c_dic[j + 1] = p
        c_oll_p += p
    companies.append(Comp(c_name, c_dic, c_oll_p))
    profit_oll_comp_av += companies[i].profit_oll

profit_oll_comp_av /= n

print(f'Средняя прибыль за год по всем предприятиям = {profit_oll_comp_av}')

print('Придприятия с прибылью выше среднего:')
for cp in companies:
    if cp.profit_oll > profit_oll_comp_av:
        print(f'Компания {cp.name} заработала {cp.profit_oll}')

print('Придприятия с прибылью ниже среднего:')
for cp in companies:
    if cp.profit_oll < profit_oll_comp_av:
        print(f'Компания {cp.name} заработала {cp.profit_oll}')

