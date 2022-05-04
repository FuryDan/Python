n = int(input())
summa = 0
for i in range(1, n, 2):
    summa += i
    summa -= i+1
if n % 2 != 0:
    print(summa + n)
else:
    print(summa)