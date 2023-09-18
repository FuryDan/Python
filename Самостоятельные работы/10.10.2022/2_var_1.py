n = int(input("Кол-во контейнеров для отходов: "))
safe = list(range(n)) 
safe[0] = 2 
safe[1] = 3 
for i in range(2, n): 
   safe[i] = safe[i-1] + safe[i-2]
print(f'Кол-во безопасных стопок: {safe[-1]}')