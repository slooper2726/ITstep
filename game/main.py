from random import randint

number = randint(1, 100)
print('Привіт! Я загадав число від 1 до 100. Спробуй вгадати його!')
while True:
    user_number = int(input('Введи число: '))
    if user_number > number:
        print('Загадане число менше твого')
    elif user_number < number:
        print('Загадане число більше твого')
    else:
        print('Ти вгадав число!')
        break
