"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input('Введите число: '))
count = 0
dec = 1
i = 1

while not (number == i):
    i = number % dec
    dec *= 10
res = ''
i = 1
while i != (dec / 10):
    i = i * 10
    res += str(int((number % (i)) // (i / 10)))
print(res)


# Решение рекурсивным методом
def calc_len_number(number_inp, len_num=1):
    res_number = number_inp % len_num
    if number_inp == res_number:
        return len_num
    else:
        len_num *= 10
        return calc_len_number(number_inp, len_num)


len_num = calc_len_number(number)


def revers_number(number_input, calc_len=1, res_str='', len_number=len_num):
    calc_len *= 10
    if calc_len == len_number * 10:
        return res_str
    else:
        res_str += str(int((number_input % calc_len) // (calc_len / 10)))
        return revers_number(number_input, calc_len, res_str)


print(revers_number(number))
