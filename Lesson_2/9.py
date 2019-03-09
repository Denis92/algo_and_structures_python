"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
number = 195
count = 0
dec = 1
i = 1
while not (number == i):
    i = number % dec
    dec *= 10
res = ''
i = 1
sum_number = 0
while i != (dec / 10):
    i = i * 10
    sum_number += (int((number % (i)) // (i / 10)))
print(f'{sum_number}')


# Решение рекурсивным методом
def calc_len_number(number_inp, len_num=1):
    res_number = number_inp % len_num
    if number_inp == res_number:
        return len_num
    else:
        len_num *= 10
        return calc_len_number(number_inp, len_num)


len_num = calc_len_number(number)


def calc_summ_number(number_input, calc_len=1, sum_number=0, len_number=len_num):
    calc_len *= 10
    if calc_len == len_num * 10:
        return sum_number
    else:
        sum_number += (int((number % (calc_len)) // (calc_len / 10)))
        return calc_summ_number(number_input, calc_len, sum_number)


print(calc_summ_number(number))
