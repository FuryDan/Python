str = '( 3tt(4t3)t(43)34(t)43(t)34t{43}t{4}t{4{4}{4}43{43}t{43{43{tb{et{3r[g rgbr3[4[4t]4{43{t}43}tb]det(e[re[g{{r}g}efb{g}]ge ])r]g}r}bg}ser}sr}ebg}er)'
stack = []

for ch in str:
    if ch in '{([':
        stack.append(ch)
    elif ch == ')':
        if (stack[-1] == '(') and (len(stack) > 0): stack.pop()
    elif ch == '}':
        if (stack[-1] == '{') and (len(stack) > 0): stack.pop()
    elif ch == ']':
        if (stack[-1] == '[') and (len(stack) > 0): stack.pop()

print(len(stack) == 0)