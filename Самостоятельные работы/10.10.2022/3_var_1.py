n = int(input("Кол-во строк треугольника Паскаля: "))
start = ["1"]
print(f'Ваш трегольник Паскаля, содержащий {n} строк:')
print(start[0])
for i in range(n - 1):
    start_1 = start.copy()
    start.clear()
    start = [str(int(start_1[j]) + int(start_1[j + 1])) for j in range(len(start_1) - 1)]
    start.insert(0, '1')
    start.append('1')
    print('\t'.join(start))