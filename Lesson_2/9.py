"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
n = int(input('Введите количество чисел, которое Вы будете вводить: '))
count = 0
dec = 1
i = 1
counter = 0
max_sum = 0
res_num = 0
while counter != n:
    number = int(input('Введите число: '))
    while not (number == i):
        i = number % dec
        dec *= 10
    i = 1
    sum_number = 0
    while i != (dec / 10):
        i = i * 10
        sum_number += (int((number % (i)) // (i / 10)))
    if sum_number > max_sum:
        max_sum = sum_number
        res_num = number
    counter += 1
print(f'Число с максимальной суммой = {res_num}\nСумма его цифр = {max_sum}')


# Решение рекурсивным методом
max_sum = 0
def calc_len_number(number_inp, len_num=1):
    res_number = number_inp % len_num
    if number_inp == res_number:
        return len_num
    else:
        return calc_len_number(number_inp, len_num * 10)


def calc_summ_number(number_input, len_number, calc_len=1, sum_number=0):
    if calc_len == len_number * 10:
        return sum_number
    else:
        calc_len *= 10
        sum_number += (int((number_input % (calc_len)) // (calc_len / 10)))
        return calc_summ_number(number_input, len_number, calc_len, sum_number)


def user_input(n, counter=0, res_num = 0, max_sum = 0):
    if n == counter:
        return f'Число с максимальной суммой = {res_num}\nСумма его цифр = {max_sum}'
    else:
        user_number = int(input('Введите число: '))
        len_num = calc_len_number(user_number)
        calc_summ = calc_summ_number(user_number, len_num)
        if calc_summ > max_sum:
            max_sum = calc_summ
            res_num = user_number
        return user_input(n, counter + 1,  res_num, max_sum)


print(user_input(n))
