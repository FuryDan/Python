m = int(input())
n = int(input())
if m % 17 == 0 or n % 17 == 0 or m % 10 == 9 or n % 10 == 9 or (m % 3 == 0 and m % 5 ==0 ) or (n % 3 == 0 and n % 5 ==0 ):
    for i in range(m,n+1,1):
        print(i)