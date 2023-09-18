T = [29, 15, 17, 12, 30, 28]

n = len(T)
ans = [0]*n
stack = []
for i in range(n-1, -1, -1):
    while stack and T[stack[-1]] <= T[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] - i
    else:
        ans[i] = 0
    stack.append(i)

print(ans)