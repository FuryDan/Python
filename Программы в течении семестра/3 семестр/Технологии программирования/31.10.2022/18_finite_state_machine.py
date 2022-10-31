list_words = ["aba", "cdfk", "abccba"]
list_float = [0.1, 5.32, 1.12]
step_1 = map(lambda x : x**2, list_float)
step_2 = map(lambda x : round(x, 1), step_1)
print(list(step_2))