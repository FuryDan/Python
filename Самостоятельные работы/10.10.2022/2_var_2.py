var = [0, 3, 8, 22]

n = int(input("Введите количество контейнеров: "))
for i in range(4, n + 1):
    var.append(2*(var[i-1] + var[i-2]))

print(f"Количество безопасных вариантов: {var[n]}")