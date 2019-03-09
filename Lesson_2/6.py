"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random

rand_number = random.randint(0, 100)
step = 0
print('Попробуйте угадать число, которое я загадал')
while step != 10:
    user_number = int(input('Введите число от 0 до 100: '))
    if user_number == rand_number:
        print('Поздравляю! Вы угадали')
        break
    elif user_number > rand_number:
        print('Вы не угадали, попробуйте ещё раз.\nПодсказка: Загаданое число меньше введенного ')
    elif user_number < rand_number:
        print('Вы не угадали, попробуйте ещё раз.\nПодсказка: Загаданое число больше введенного ')
    step += 1
if step >= 10:
    print(f'Было загадано число {rand_number}')


# Решение рекурсивным методом

def puzzle(count_step=0, step=10):
    if count_step == step:
        return f'Было загадано число {rand_number}'
    else:
        user_num = int(input('Введите число от 0 до 100: '))
        if user_num == rand_number:
            print('Поздравляю! Вы угадали')
            return 1
        elif user_num > rand_number:
            print('Вы не угадали, попробуйте ещё раз.\nПодсказка: Загаданое число меньше введенного ')
        elif user_num < rand_number:
            print('Вы не угадали, попробуйте ещё раз.\nПодсказка: Загаданое число больше введенного ')
        count_step += 1
        return puzzle(count_step)


puzzle()
