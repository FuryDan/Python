from math import log
n = int(input())
summa = 0
for i in range(1, n+1):
    summa += 1/i
summa -= log(n)
print(summa)