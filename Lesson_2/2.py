"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input('Введите число: '))
count = 0
dec = 1
i = 1
while not (number == i):
    i = number % dec
    dec *= 10
i = 1
count_even = 0
count_odd = 0
while i != (dec / 10):
    i = i * 10
    if (int((number % (i)) // (i / 10))) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'Количество четных цифр: {count_even}\nКоличество нечетных цифр: {count_odd}')


# Решение рекрсивным методом
def calc_len_number(number_inp, len_num=1):
    res_number = number_inp % len_num
    if number_inp == res_number:
        return len_num
    else:
        return calc_len_number(number_inp, len_num * 10)


len_num = calc_len_number(number)


def calc_even_odd(number_inp=number, calc_len=1, count_even_f=0, count_odd_f=0, len_number=len_num, ):
    calc_len *= 10
    if calc_len == len_number * 10:
        return f'Количество четных цифр: {count_even_f}\nКоличество нечетных цифр: {count_odd_f}'
    else:
        if int((number_inp % calc_len) // (calc_len / 10)) % 2 == 0:
            return calc_even_odd(number_inp, calc_len, count_even_f + 1, count_odd_f)
        else:
            return calc_even_odd(number_inp, calc_len, count_even_f, count_odd_f + 1)


print(calc_even_odd(number))
