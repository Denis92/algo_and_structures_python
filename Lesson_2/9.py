"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
n = int(input('Введите количество чисел, которое Вы будете вводить: '))

counter = 0
max_sum = 0
res_num = 0
while counter != n:
    number = int(input('Введите число: '))
    sum_number = 0
    dec = 1
    while number % dec != number:
        dec *= 10
        sum_number += (int(number % dec // (dec / 10)))
    if sum_number > max_sum:
        max_sum = sum_number
        res_num = number
    counter += 1
print(f'Число с максимальной суммой = {res_num}\nСумма его цифр = {max_sum}')


# Решение рекурсивным методом
def calc_summ_number(number_input, dec=1, sum_number=0):
    if number_input % dec == number_input:
        return sum_number
    else:
        dec *= 10
        sum_number += (int(number_input % dec // (dec / 10)))
        return calc_summ_number(number_input, dec, sum_number)


def user_input(n, counter=0, res_num=0, max_sum=0):
    if n == counter:
        return f'Число с максимальной суммой = {res_num}\nСумма его цифр = {max_sum}'
    else:
        user_number = int(input('Введите число: '))
        res_summ = calc_summ_number(user_number)
        if res_summ > max_sum:
            res_num = user_number
            max_sum = res_summ

        return user_input(n, counter + 1, res_num, max_sum)


print(user_input(n))
