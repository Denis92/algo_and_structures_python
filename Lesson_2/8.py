"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
# Решение строковым методом, в данном случае я не использую списки(массивы),
# возможно данное решение будет не совсем честным,поэтому предложу ещё один вариант

n = int(input('Введите количество чисел, которое Вы будете вводить: '))
find_num = input('Введите искомую цифру: ')
i = 0
count_number = 0
while i != n:
    user_number = input('Введите число: ')
    for j in user_number:
        if j == find_num:
            count_number += 1
    i += 1

print(f'Искомая цифра {find_num} повторяется {count_number} раз(а)')

# Второй вариант решения через деление и взятие остатка

count_number = 0
dec = 1
temp_num = 1
i = 0
while i != n:
    user_number = int(input('Введите число: '))
    while not (user_number == temp_num):
        temp_num = user_number % dec
        dec *= 10
    j = 1
    while j != (dec / 10):
        j *= 10
        if (int((user_number % (j)) // (j / 10))) == int(find_num):
            count_number += 1
    i += 1

print(f'Искомая цифра {find_num} повторяется {count_number} раз(а)')


# Решение рекурсивным методом, в данном случае реализую через рекурсию только ввод данных

def user_input(n, counter=0, count_number=0):
    if n == counter:
        return f'Искомая цифра {find_num} повторяется {count_number} раз(а)'
    else:
        dec = 1
        temp_num = 1
        user_number = int(input('Введите число: '))
        while not (user_number == temp_num):
            temp_num = user_number % dec
            dec *= 10
        j = 1
        while j != (dec / 10):
            j *= 10
            if (int((user_number % (j)) // (j / 10))) == int(find_num):
                count_number += 1
        return user_input(n, counter + 1, count_number)


print(user_input(n))
