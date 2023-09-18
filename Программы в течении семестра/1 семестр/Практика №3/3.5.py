from math import *
chisl = float(input())
if chisl < 0:
    print('Число не положительно')
else:
    n = floor(chisl)
    ost = chisl - n
    print(ost)