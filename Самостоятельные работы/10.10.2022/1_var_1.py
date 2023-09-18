def steps(n):
    a, b, c = 0, 1, 1
    if n < 2:
        return [a, b, c][n]
    while n:
        a, b, c = b, c, a+b+c
        n -= 1
    return b

n = int(input("Кол-во ступенек лесенки: "))
print(f'Кол-во способов спуститься: {steps(n)}')