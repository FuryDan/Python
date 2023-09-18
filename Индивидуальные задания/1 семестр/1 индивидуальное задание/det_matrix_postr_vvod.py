from math import ceil
import copy


def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):
    m = len(A)
    n = len(A[0])
    if n == 1:
        return A[0][0]
    mn = 1
    determinant = 0
    for j in range(n):
        determinant += A[0][j] * mn * det(minor(A, 0, j))
        mn *= -1
    return determinant


def parting(xs, n):
    part_len = ceil(len(xs)/n)
    return [xs[part_len*k:part_len*(k+1)] for k in range(n)]


n = int(input('Матрица размером N x N.\nВведите n: '))
if n == 0:
    print('Размер матрицы не может быть 0 х 0.')
    exit()
if n < 0:
    print('Размер матрицы не может принимать отрицательные значения.')
    exit()
if n > 10:
    print('Размер матрицы не может превышать размер 10 х 10 по условию.')
    exit()
if n <= 10:
    element = input('Введите элементы матрицы, разделенных пробелом: ').split()
    if len(element) != n**2:
        print('Введенное количество элементов не соответствуют следующему условию: "Введенное количество элементов" = n^2 ')
        exit()
    else:
        xs = list(map(int, element))
        print('\nВаша матрица: ')
        for strA in parting(xs, n):
            print(strA)
        A = parting(xs, n)
        print('\nОпределитель матрицы:', det(A))
        exit()