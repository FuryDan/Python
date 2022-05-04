mylist = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(mylist)+1):
    print(i*mylist[i-1])