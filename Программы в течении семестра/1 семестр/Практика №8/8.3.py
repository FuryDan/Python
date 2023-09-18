str = input()
flag = False
for i in range(len(str)):
    if str[i] in '0123456789':
        flag = True
if flag is True:
    print('YES')
else:
    print('NO')