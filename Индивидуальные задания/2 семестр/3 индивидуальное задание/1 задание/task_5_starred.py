import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def geoSum(a1, n):
    return a1 / n**2


def f_n(n: int):
    return geoSum(1, n)


# Константы для работы алгоритмов
mark = True
run_n = 1
eps = 1e-15
delta = 0
x, y = [], []
s_y = []

# Поиск предела через sympy >> 'pip install -U sympy'
n = Symbol("x")
lim = float(limit(f_n(n), n, oo))
print(lim)

# Формирование точек
while mark:
    run_n = (run_n + 1)
    an = f_n(run_n)
    if len(y) > 0:
        delta = abs(y[-1] - an)
        s_y.append(s_y[-1] + an)
    else:
        s_y.append(an)
    x.append(run_n)
    y.append(float(an))
    if (delta > 0) and (delta < eps): mark = False
lim_f = round(y[-1], 6)
print(an, delta, run_n)
print(lim_f, lim)

# Вывод функции
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
ax_2 = fig.add_subplot(2, 1, 2)
ax.grid(True)
ax_2.grid(True)
ax.scatter(x, y, color='black', marker='*', linewidth=0.5)
ax_2.scatter(x, s_y, color='brown', marker='*', linewidth=0.5)
ax.plot(np.linspace(0, len(x)*1.05), np.linspace(lim_f, lim_f), linewidth=1.5, color='red')
plt.show()