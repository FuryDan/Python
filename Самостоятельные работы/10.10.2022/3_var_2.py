def count_attempts(x,y,N):
    if y==8:
        return N
    if x==1:
        return count_attempts(2, y+1, N)
    if x==8:
        return count_attempts(7, y+1, N)
    return (count_attempts(x+1, y+1, N) + count_attempts(x-1, y+1, N))

x = int(input("Введите x: "))
y = int(input("Введите y: "))
print(f"Количество способов добраться до верха поля: {count_attempts(x,y,1)}")