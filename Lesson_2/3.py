"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input('Введите число: '))
count = 0
dec = 1
i = 1
res = ''
while number % dec != number:
    dec *= 10
    res += str(int(number % dec//(dec/10)))
print(res)


# Решение рекурсивным методом
def revers_number(number_inp, dec = 10, res = ''):
    if number_inp % dec >= number_inp:
        return res + str(int(number % dec // (dec / 10)))
    else:
        res += str(int(number % dec // (dec / 10)))
        return revers_number(number_inp, dec * 10, res)


print(revers_number(number))
