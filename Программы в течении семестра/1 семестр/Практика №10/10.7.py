n = int(input('Введите число: '))
dels = []
for i in range(1, n+1):
    if n % i == 0:
        dels.append(i)
print(dels)