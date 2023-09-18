def trip(x, y, z):
    return x * 100 + y * 10 + z


abc = int(input())
a = abc // 100
b = abc % 100 // 10
c = abc % 10
print(trip(a, b, c), trip(a, c, b), trip(b, a, c), trip(b, c, a), trip(c, b, a), trip(c, a, b), sep=' / ')