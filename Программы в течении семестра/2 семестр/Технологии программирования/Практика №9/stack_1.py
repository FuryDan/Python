L = input('Введите элементы через пробел: ').split()
k = int(input('Введите количество отображаемых элементов: '))
A, B = [], []
for i in range(k):
  A.append(L[i])
for i in range(k, len(L)):
  if not B:
    while A:
      B.append(A.pop())
    B.pop()
    A.append(L[i])
  else:
    B.pop()
    A.append(L[i])
  print(B[::-1], A)