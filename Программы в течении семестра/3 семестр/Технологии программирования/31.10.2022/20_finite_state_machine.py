word = input("Введите слово: ")
print("Первая буква а?", *map(lambda x : x.lower() == "а", word[0]))