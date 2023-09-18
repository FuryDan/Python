n = int(input())
summa = 1 + n
for i in range(2, round(n / 2) + 1):
    if n % i == 0:
        summa += i
print(summa)