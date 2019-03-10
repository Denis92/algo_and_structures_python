"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input('Введите число: '))
count = 0
dec = 1
i = 1
count_even = 0
count_odd = 0
while number % dec != number:
    dec *= 10
    if (int((number % dec) // (dec / 10))) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'Количество четных цифр: {count_even}\nКоличество нечетных цифр: {count_odd}')


# Решение рекурсивным методом
def calc_even_odd(number_inp, dec=1, count_even_r=0, count_odd_r=0):
    if number_inp % dec == number_inp:
        return f'Количество четных цифр: {count_even_r}\nКоличество нечетных цифр: {count_odd_r}'
    else:
        dec *= 10
        if (int((number_inp % dec) // (dec / 10))) % 2 == 0:
            return calc_even_odd(number_inp, dec, count_even_r + 1, count_odd_r)
        else:
            return calc_even_odd(number_inp, dec, count_even_r, count_odd_r + 1)


print(calc_even_odd(number))
