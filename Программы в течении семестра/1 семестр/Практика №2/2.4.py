chisl = int(input())
d4 = chisl % 10
d3 = chisl % 100 // 10
d2 = chisl % 1000 //100
d1 = chisl // 1000
if d1 + d4 == d2 + d3:
    print('Условие выполнено')
else:
    print('Условие не выполнено')