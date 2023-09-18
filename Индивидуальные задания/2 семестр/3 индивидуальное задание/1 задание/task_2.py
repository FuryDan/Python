from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def f_n(n: int):
    return ((3 - n)**2 + (3 + n)**2) / ((3 - n)**2 - (3 + n)**2)

# Константы для работы алгоритмов
mark = True
run_n = 1
eps = 1e-7
delta = 0
x, y = [], []

# Поиск предела через sympy >> 'pip install -U sympy'
n = Symbol("x")
lim_f = float(limit(f_n(n), n, oo))
print(lim_f)

# Формирование точек
while mark:
    run_n = (run_n + 1)
    an = f_n(run_n)
    if len(y) > 1:
        delta = abs(y[-1] - an)
    x.append(run_n)
    y.append(an)
    if (delta > 0) and (delta < eps): mark = False
lim_f = round(y[-1], 2)
print(an, delta, run_n)
print(lim_f)


# Вывод функции
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.scatter(x, y, color='blue', marker='.', linewidth=0.5)

plt.show()