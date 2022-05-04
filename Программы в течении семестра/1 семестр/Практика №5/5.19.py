n = int(input())
max1 = 1
max2 = 1
for i in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    else:
        if num > max2:
            max2 = num
print(max1, max2)