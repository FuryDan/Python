fib = [1, 2]

n = int(input('2^n, n = ? | int >> '))
for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])

print(fib[n])