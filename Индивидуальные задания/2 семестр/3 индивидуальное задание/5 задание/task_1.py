import numpy as np
from math import *
import matplotlib.pyplot as plt

# Ввод функции
def f_x(x):
    return 2 * x**3 - 9 * x**2 + 12 * x - 9


def g_x(x: np.linspace, a: list):
    y = 0
    for i in range(len(a)):
        y += float(a[i])*(x**i)
    return y


def f1_x(x0):
    dx = 1e-3
    return (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx


t = 5000
x = np.linspace(-0.75, 1.75, 300)
x1 = np.linspace(-0.25, 1.25, t)
y = f_x(x)
y1 = f1_x(x1)

# Поиск x, где производная = 0
pts = [[], [], []]
for x0 in range(len(y1)):
    xt = -0.25 + (x0 * 1.5 / t)
    if round(y1[x0], 2) == 0:
        if len(pts[0]) == 0:
            pts[0].append(xt)
            pts[1].append(f_x(xt))
            pts[2].append(x0)
        elif (x0 - pts[2][-1] > 2):
            pts[0].append(xt)
            pts[1].append(f_x(xt))
            pts[2].append(x0)
        else:
            pts[0][-1] = 0.5 * (pts[0][-1] + xt)
            pts[1][-1] = 0.5 * (pts[1][-1] + f_x(xt))
            pts[2][-1] = x0

# Поиск доп. точек
x_t = pts[0][1] + abs(pts[0][1] - pts[0][2])
pts[0].append(x_t)
pts[1].append(f_x(x_t))
x_t = pts[0][0] - abs(pts[0][0] - pts[0][1])
pts[0].append(x_t)
pts[1].append(f_x(x_t))

# Построение эскиза
print(pts)
M = []
for i in range(len(pts[0])):
    mi = [np.power(pts[0][i], _, dtype=np.float64) for _ in range(len(pts[0]))]
    M.append(mi)

X_m = np.linalg.solve(M, np.array(pts[1]))
x_m = np.linspace(np.min(pts[0]) - 0.15, np.max(pts[0]) + 0.15, 100)

# Построение графика
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, linewidth=1.5, color='red')
ax.plot(x1, y1, linewidth=1, color='green')
ax.plot(x_m, g_x(x_m, X_m), linewidth=1, color='black')
ax.scatter(pts[0], pts[1], linewidth=1, color='blue', marker='*')

plt.show()