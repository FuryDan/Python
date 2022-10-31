from random import randrange


n = int(input('Количество строк \ int >> '))
m = int(input('Количество столбцов \ int >> '))

ans = [[0 for __ in range(n)] for _ in range(m)]

price = [[randrange(10, 50) for __ in range(n)] for _ in range(m)]
ans[0][0] = [1, price[0][0]];

for i in range(1, n):
    ans[0][i] = [1, ans[0][i-1][1] + price[0][i]]
for i in range(1, m):
    ans[i][0] = [1, ans[i-1][0][1] + price[i][0]]
for i in range(1, m):
    for j in range(1, n):
        ans[i][j] = [ans[i-1][j][0] + ans[i][j-1][0], max(ans[i-1][j][1], ans[i][j-1][1]) + price[i][j]]

print('Ответ:', ans[m-1][n-1])
print('Исходная таблица:')
for i in range(m):
    s = ''
    for j in range(n):
        s += str(ans[i][j][0]).rjust(4) + '|' + str(price[i][j]).rjust(2) + '|' + str(ans[i][j][1]).ljust(7)
    print(s)