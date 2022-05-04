#Определяет возраст без вложенных или каскадных условий
vozvr = int(input())
if vozvr <= 13:
    print('Детство')
if vozvr >=14 and vozvr <=24:
    print('Молодость')
if vozvr >= 25 and vozvr <= 59:
    print('Зрелость')
if vozvr >=60:
    print('Старость')

#Определяет возраст с вложенным условием
vozvr = int(input())
if vozvr <= 13:
    print('Детство')
else:
    if vozvr <= 24:
        print('Молодость')
    else:
        if vozvr <=59:
            print('Зрелость')
        else:
            print('Старость')

#Определяет возраст с вложенным условием
vozvr = int(input())
if vozvr <= 13:
    print('Детство')
elif vozvr <=24:
    print('Молодость')
elif vozvr <= 59:
    print('Зрелость')
else:
    print('Старость')