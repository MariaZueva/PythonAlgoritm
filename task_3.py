""" По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки. """
# https://drive.google.com/file/d/1Niz_pp9UiCiOnihNseReXbUnyvjV05Je/view?usp=sharing

x0 = float(input('Коодината первой точки: x0 = '))
y0 = float(input('Коодината первой точки: y0 = '))
x1 = float(input('Коодината второй точки: x1 = '))
y1 = float(input('Коодината ыторой точки: y1 = '))

a = (y1 - y0) / (x1 - x0)
b = y0 - a * x0

print(f'Уранение прямой: y = {a} * x + {b}')

