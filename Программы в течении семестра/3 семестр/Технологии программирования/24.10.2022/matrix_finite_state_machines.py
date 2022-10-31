def matrix(m, n, value):
    matr = []
    if m == n:
        a = [value for i in range(n)]
        if n == 1:
            return value
        if n > 1:
            for i in range(n):
                matr.append(a)

        for i in range(n):
            print(*matr[i])
    else:
        a = [value for i in range(m)]
        for i in range(n):
            matr.append(a)

        for i in range(n):
            print(*matr[i])


matrix(m = int(input("Введите кол-во столбцов: ")), n = int(input("Введите кол-во строк: ")), value = 0)