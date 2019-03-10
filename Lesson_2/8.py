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
i = 0
while i != n:
    user_number = int(input('Введите число: '))
    dec = 1
    while user_number != user_number % dec:
        dec *= 10
        if (int((user_number % dec) // (dec / 10))) == int(find_num):
            count_number += 1
    i += 1

print(f'Искомая цифра {find_num} повторяется {count_number} раз(а)')


# Решение рекурсивным методом

def find_num_func(user_num, find_num, dec=1, count_num=0):
    if user_num == user_num % dec:
        return count_num
    else:
        dec *= 10
        if (int((user_num % dec) // (dec / 10))) == int(find_num):
            count_num += 1
        return find_num_func(user_num, find_num, dec, count_num)


def user_input(n, find_num, counter=0, count_number=0):
    if n == counter:
        return f'Искомая цифра {find_num} повторяется {count_number} раз(а)'
    else:
        user_number = int(input('Введите число: '))
        return user_input(n, find_num, counter + 1, count_number + find_num_func(user_number, find_num))


print(user_input(n, find_num))
