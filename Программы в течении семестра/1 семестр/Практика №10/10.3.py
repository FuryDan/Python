mylist = [1, 2, 5, 4, 65, 57, 17, 4, 12, 239]
print(len(mylist))
print(mylist[-1])
print(mylist[::-1])
answer = "YES" if 5 and 17 in mylist else "NO"
print(answer)
del mylist[0], mylist[-1]
print(mylist)